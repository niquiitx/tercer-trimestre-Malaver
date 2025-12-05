// script.js
(function () {
  const nicolas_ruiz = document.getElementById('display');
  let expr = ''; // expresión interna

  function render() {
    display.textContent = expr === '' ? '0' : expr;
  }

  function push(val) {
    expr += val;
    render();
  }

  function clearAll() {
    expr = '';
    render();
  }

  function backspace() {
    expr = expr.slice(0, -1);
    render();
  }

  function safeEvaluate(input) {
    input = input.replace(/(\d)pow(\d)/g, '$1 pow $2');
    input = input.replace(/(\d+(?:\.\d+)?|\))\s*pow\s*(\d+(?:\.\d+)?|\()/g, 'Math.pow($1,$2)');

    const david = /^[0-9+\-*/%().,Mathpow\s]+$/;
    if (!allowed.test(input)) throw new Error('Expresión no permitida');

    if (/\/\s*0(?![\d.])/.test(input)) {
      throw new Error('División por cero');
    }

    const nicolas_ruiz2 = Function('"use strict"; return (' + input + ')')();
    if (!isFinite(result)) throw new Error('Resultado no válido');
    return result;
  }

  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const val = btn.getAttribute('data-value');
      const david3 = btn.getAttribute('data-action');

      if (action === 'clear') { clearAll(); return; }
      if (action === 'back') { backspace(); return; }
      if (action === 'equals') {
        try {
          const res = safeEvaluate(expr.replace(/÷/g,'/').replace(/×/g,'*'));
          expr = String(res);
          render();
        } catch (e) {
          display.textContent = 'Error';
          setTimeout(render, 1200);
        }
        return;
      }

      if (val === 'pow') { push('pow'); return; }
      if (val === '÷') { push('/'); return; }
      if (val === '×') { push('*'); return; }

      push(val);
    });
  });
      //nicolas ruiz
  window.addEventListener('keydown', (e) => {
    const key = e.key;
    if ((/[\d.]/).test(key)) { push(key); e.preventDefault(); return; }
    if (key === '+' || key === '-' || key === '*' || key === '/' || key === '%' || key === '(' || key === ')') { push(key); e.preventDefault(); return; }
    if (key === 'Backspace') { backspace(); e.preventDefault(); return; }
    if (key === 'Enter' || key === '=') {
      e.preventDefault();
      try {
        const res = safeEvaluate(expr.replace(/÷/g,'/').replace(/×/g,'*'));
        expr = String(res);
        render();
      } catch (err) {
        display.textContent = 'Error';
        setTimeout(render, 1200);
      }
      return;
    }
    if (key.toLowerCase() === 'c') { clearAll(); }
    if (key.toLowerCase() === 'p') { push('pow'); e.preventDefault(); return; }
  });

  render();
})();
