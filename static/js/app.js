"use strict";

(function () {
    const EL_INPUT = {
        zhangchangpu: document.getElementById('zhangchangpu-input'),
        mizhu: document.getElementById('mizhu-input'),
    };

    const EL_OUTPUT = {
        zhangchangpu: {
            all: document.getElementById('zhangchangpu-all'),
            best: document.getElementById('zhangchangpu-best'),
        },
        mizhu: document.getElementById('mizhu-output'),
    };

    const TABS = {
        buttons: document.querySelectorAll('.tab-button'),
        panels: document.querySelectorAll('.tab-panel'),
    };

    const HISTORY_KEY = 'zhangchangpu_history';
    const HISTORY_MAX = 10;

    let activeTab = 'zhangchangpu';

    function init() {
        initTheme();
        bindTabs();
        bindCardButtons();
        bindActionButtons();
        bindCopyButtons();
        bindKeyboard();
        bindHistory();
        updateCount('zhangchangpu');
        updateCount('mizhu');
        refreshPlaceholder('zhangchangpu');
        refreshPlaceholder('mizhu');
        EL_INPUT.zhangchangpu.focus();
    }

    /* Theme */
    function initTheme() {
        const toggle = document.getElementById('theme-toggle');
        const root = document.documentElement;
        const saved = localStorage.getItem('theme');
        if (saved === 'dark') {
            root.classList.add('dark');
        }
        toggle.addEventListener('click', () => {
            root.classList.toggle('dark');
            localStorage.setItem('theme', root.classList.contains('dark') ? 'dark' : 'light');
        });
    }

    /* Tabs */
    function bindTabs() {
        TABS.buttons.forEach((btn) => {
            btn.addEventListener('click', () => {
                const target = btn.dataset.tab;
                setActiveTab(target);
            });
        });
    }

    function setActiveTab(name) {
        activeTab = name;
        TABS.buttons.forEach((btn) => {
            const isActive = btn.dataset.tab === name;
            btn.classList.toggle('active', isActive);
            btn.setAttribute('aria-selected', String(isActive));
            btn.setAttribute('tabindex', isActive ? '0' : '-1');
        });
        TABS.panels.forEach((panel) => {
            const isActive = panel.id === `${name}-tab`;
            panel.classList.toggle('active', isActive);
            panel.hidden = !isActive;
        });
        EL_INPUT[name].focus();
    }

    /* Card buttons */
    function bindCardButtons() {
        document.querySelectorAll('.button-grid button').forEach((btn) => {
            btn.addEventListener('click', () => {
                const targetId = btn.closest('.button-grid').dataset.target;
                const input = document.getElementById(targetId);
                appendToInput(input, btn.dataset.value);
            });
        });
    }

    function appendToInput(input, value) {
        input.classList.remove('error');
        const current = input.value.trimEnd();
        input.value = current ? `${current} ${value} ` : `${value} `;
        input.focus();
        updateCountByInput(input);
    }

    /* Action buttons */
    function bindActionButtons() {
        document.querySelectorAll('.action-btn').forEach((btn) => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;
                const target = btn.dataset.target;
                if (action === 'enter') {
                    handleEnter(target);
                } else if (action === 'delete') {
                    handleDelete(target);
                } else if (action === 'backspace') {
                    handleBackspace(target);
                }
            });
        });
    }

    function setLoading(name, loading) {
        const btn = document.querySelector(`.enter-btn[data-target="${name}"]`);
        if (!btn) return;
        btn.disabled = loading;
        btn.classList.toggle('loading', loading);
        btn.textContent = loading ? '计算中…' : '确认 Enter';
    }

    function handleBackspace(name) {
        const input = EL_INPUT[name];
        const tokens = input.value.trim().split(/\s+/).filter(Boolean);
        tokens.pop();
        input.value = tokens.length ? `${tokens.join(' ')} ` : '';
        input.classList.remove('error');
        updateCount(name);
        input.focus();
    }

    function bindKeyboard() {
        Object.values(EL_INPUT).forEach((input) => {
            input.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    handleEnter(activeTab);
                } else if (e.key === 'Escape') {
                    handleDelete(activeTab);
                }
            });
            input.addEventListener('input', () => {
                input.classList.remove('error');
                updateCountByInput(input);
            });
        });

        // 当在输入框之间切换时自动更新 activeTab
        Object.entries(EL_INPUT).forEach(([name, input]) => {
            input.addEventListener('focus', () => {
                activeTab = name;
            });
        });
    }

    function getInput(name) {
        return EL_INPUT[name].value.trim();
    }

    function updateCount(name) {
        const input = EL_INPUT[name];
        updateCountByInput(input);
    }

    function updateCountByInput(input) {
        const name = input.id.replace('-input', '');
        const count = input.value.trim().split(/\s+/).filter(Boolean).length;
        const badge = document.querySelector(`.card-count[data-target="${name}"]`);
        if (badge) badge.textContent = `${count} 张`;
    }

    function setError(name, message) {
        const input = EL_INPUT[name];
        input.classList.add('error');
        const output = name === 'zhangchangpu' ? EL_OUTPUT.zhangchangpu.all : EL_OUTPUT.mizhu;
        output.innerHTML = `<span class="error">错误：${escapeHtml(message)}</span>`;
        if (name === 'zhangchangpu') {
            EL_OUTPUT.zhangchangpu.best.textContent = '';
        }
    }

    function clearError(name) {
        EL_INPUT[name].classList.remove('error');
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    async function handleEnter(name) {
        const raw = getInput(name);
        if (!raw) {
            setError(name, '请先输入牌面');
            return;
        }
        clearError(name);
        clearOutputs(name);
        setLoading(name, true);

        const endpoint = name === 'zhangchangpu' ? '/api/zhangchangpu' : '/api/mizhu';
        try {
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input: raw }),
            });
            if (!res.ok) {
                let msg = `服务器错误（${res.status}）`;
                try {
                    const err = await res.json();
                    if (err && err.error) msg = err.error;
                } catch (_) { /* ignore */ }
                setError(name, msg);
                return;
            }
            const json = await res.json();
            if (!json.success) {
                setError(name, json.error || '请求失败');
                return;
            }
            if (name === 'zhangchangpu') {
                renderZhangchangpu(json.data);
            } else {
                renderMizhu(json.data);
            }
            addHistory(name, raw, json.data);
        } catch (err) {
            setError(name, '网络请求异常，请检查服务是否运行');
        } finally {
            setLoading(name, false);
        }
    }

    function clearOutputs(name) {
        if (name === 'zhangchangpu') {
            EL_OUTPUT.zhangchangpu.all.textContent = '';
            EL_OUTPUT.zhangchangpu.best.textContent = '';
        } else {
            EL_OUTPUT.mizhu.textContent = '';
        }
    }

    function renderSummary(container, message) {
        const summary = document.createElement('div');
        summary.className = 'summary';
        summary.textContent = message;
        container.appendChild(document.createTextNode('\n'));
        container.appendChild(summary);
    }

    function renderNumberedList(items) {
        if (!items || items.length === 0) return '';
        return items.map((line, idx) => `${idx + 1}. ${line}`).join('\n');
    }

    function renderZhangchangpu(data) {
        const allEl = EL_OUTPUT.zhangchangpu.all;
        const bestEl = EL_OUTPUT.zhangchangpu.best;
        allEl.textContent = '';
        bestEl.textContent = '';

        if (!data.solutions || data.solutions.length === 0) {
            allEl.textContent = data.message || '这道题，会儿解不出来';
            return;
        }

        const solutions = data.solutions.map((s) => (Array.isArray(s) ? s.join('') : s));
        const best = (data.best_solutions || []).map((s) => (Array.isArray(s) ? s.join('') : s));

        allEl.appendChild(buildSolutionList(solutions, false));
        bestEl.appendChild(buildSolutionList(best, true));

        renderSummary(bestEl, data.message);
    }

    function buildSolutionList(items, highlight, mizhuStyle) {
        const list = document.createElement('div');
        list.className = 'solution-list';
        items.forEach((line, idx) => {
            const row = document.createElement('div');
            row.className = 'solution-row' + (highlight ? ' best' : '') + (mizhuStyle ? ' mizhu' : '');

            const num = document.createElement('span');
            num.className = 'solution-number';
            num.textContent = `${idx + 1}.`;
            row.appendChild(num);

            const match = String(line).match(/^(.+?)\s+and\s+(.+)$/);
            if (!match) {
                row.appendChild(buildCardGroup(line));
                list.appendChild(row);
                return;
            }

            row.appendChild(buildCardGroup(match[1]));
            const eq = document.createElement('span');
            eq.className = 'solution-equals';
            eq.textContent = '=';
            row.appendChild(eq);
            row.appendChild(buildCardGroup(match[2]));

            list.appendChild(row);
        });
        return list;
    }

    function buildCardGroup(expression) {
        const group = document.createElement('span');
        group.className = 'card-group';
        expression.split('+').forEach((value) => {
            const card = document.createElement('span');
            card.className = 'card-chip';
            card.textContent = value.trim();
            group.appendChild(card);
        });
        return group;
    }

    function renderMizhu(data) {
        const el = EL_OUTPUT.mizhu;
        el.textContent = '';
        if (!data.combinations || data.combinations.length === 0) {
            el.textContent = data.message || '这道题，冲儿解不出来';
            return;
        }
        el.appendChild(buildSolutionList(data.combinations.map((item) => item.text), false, true));
        renderSummary(el, data.message);
    }

    function handleDelete(name) {
        EL_INPUT[name].value = '';
        clearError(name);
        clearOutputs(name);
        updateCount(name);
        refreshPlaceholder(name);
        EL_INPUT[name].focus();
    }

    function refreshPlaceholder(name) {
        const list = DIALOGUES[name] || [];
        if (list.length === 0) return;
        const line = list[Math.floor(Math.random() * list.length)];
        EL_INPUT[name].placeholder = line;
    }

    /* Copy buttons */
    function bindCopyButtons() {
        document.querySelectorAll('.copy-btn').forEach((btn) => {
            btn.addEventListener('click', async () => {
                const targetId = btn.dataset.copyTarget;
                const el = document.getElementById(targetId);
                const text = el.textContent || '';
                try {
                    await navigator.clipboard.writeText(text);
                    const original = btn.textContent;
                    btn.textContent = '已复制';
                    setTimeout(() => (btn.textContent = original), 1200);
                } catch (err) {
                    btn.textContent = '复制失败';
                    setTimeout(() => (btn.textContent = '复制'), 1200);
                }
            });
        });
    }

    /* History */
    function bindHistory() {
        const toggle = document.getElementById('history-toggle');
        const panel = document.getElementById('history-panel');
        const clearBtn = document.getElementById('history-clear');

        toggle.addEventListener('click', () => {
            const expanded = toggle.getAttribute('aria-expanded') === 'true';
            toggle.setAttribute('aria-expanded', String(!expanded));
            panel.hidden = expanded;
            toggle.querySelector('.history-chevron').textContent = expanded ? '▶' : '▼';
        });

        clearBtn.addEventListener('click', () => {
            localStorage.removeItem(HISTORY_KEY);
            renderHistory();
        });

        renderHistory();
    }

    function getHistory() {
        try {
            return JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]');
        } catch (_) {
            return [];
        }
    }

    function addHistory(name, raw, data) {
        const history = getHistory();
        const label = name === 'zhangchangpu' ? '张菖蒲' : '糜竺';
        const count = data.input_count ?? data.input?.length ?? 0;
        history.unshift({
            name,
            label,
            raw,
            count,
            timestamp: new Date().toISOString(),
        });
        if (history.length > HISTORY_MAX) history.pop();
        localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
        renderHistory();
    }

    function renderHistory() {
        const list = document.getElementById('history-list');
        const history = getHistory();
        list.innerHTML = '';
        if (history.length === 0) {
            list.innerHTML = '<li class="history-empty">暂无历史记录</li>';
            return;
        }
        history.forEach((item) => {
            const li = document.createElement('li');
            li.className = 'history-item';
            li.innerHTML = `<span class="history-label">${escapeHtml(item.label)}</span>
                            <span class="history-raw">${escapeHtml(item.raw)}</span>
                            <span class="history-count">${item.count} 张</span>`;
            li.addEventListener('click', () => {
                setActiveTab(item.name);
                EL_INPUT[item.name].value = `${item.raw} `;
                updateCount(item.name);
            });
            list.appendChild(li);
        });
    }

    init();
})();
