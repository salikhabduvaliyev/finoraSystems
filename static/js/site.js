// Finora Systems — sayt effektlari va ariza formalari
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  // Tarjima qilingan matnlar (base.html dagi json_script'dan); topilmasa — o'zbekcha
  var T = {};
  try { T = JSON.parse(document.getElementById('fs-i18n').textContent); } catch (e) {}
  function t(k, d) { return T[k] || d; }
  function esc(x) { var d = document.createElement('div'); d.textContent = x; return d.innerHTML; }

  var nav = $('.nav'), burger = $('#bg'), up = $('#up'), pg = $('#pg'), header = $('header');

  // Mobil menyu
  if (burger) burger.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Tepaga tugmasi, progress chizig'i, header soyasi
  if (up) up.addEventListener('click', function () { scrollTo({ top: 0, behavior: 'smooth' }); });
  addEventListener('scroll', function () {
    var h = document.documentElement, y = scrollY;
    pg.style.width = Math.min(100, y / Math.max(1, h.scrollHeight - innerHeight) * 100) + '%';
    header.classList.toggle('sc', y > 10);
    up.classList.toggle('on', y > 500);
  }, { passive: true });

  // Kartalarda sichqoncha ortidan yorug'lik
  addEventListener('mousemove', function (e) {
    var c = e.target.closest && e.target.closest('.card,.cc,.ts');
    if (!c) return;
    var r = c.getBoundingClientRect();
    c.style.setProperty('--mx', e.clientX - r.left + 'px');
    c.style.setProperty('--my', e.clientY - r.top + 'px');
  });

  // Keyslar karuseli
  $$('[data-scroll]').forEach(function (b) {
    b.addEventListener('click', function () {
      var cs = $('#cs'); if (cs) cs.scrollBy({ left: 360 * +b.dataset.scroll, behavior: 'smooth' });
    });
  });

  // Ko'rinishga kirganda paydo bo'lish + raqamlar animatsiyasi
  function countUp(t) {
    if (!t.classList.contains('sb')) return;
    var b = t.querySelector('b'), m = b && b.textContent.match(/^(\d+)(.*)$/);
    if (!m) return;
    var n = +m[1], st = performance.now();
    (function f(now) {
      var p = Math.min((now - st) / 1300, 1);
      b.textContent = Math.round(n * (1 - Math.pow(1 - p, 3))) + m[2];
      if (p < 1) requestAnimationFrame(f);
    })(st);
  }
  if (!matchMedia('(prefers-reduced-motion:reduce)').matches && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var t = e.target; io.unobserve(t); t.classList.add('in'); countUp(t);
        setTimeout(function () { t.classList.remove('rv', 'in'); t.style.transitionDelay = ''; }, 1500);
      });
    }, { threshold: .1, rootMargin: '0px 0px -30px 0px' });
    $$('#app .card,#app .ts,#app .cc,#app .sb,#app .pcard,#app .pt,#app .ct,#app .eyebrow,#app section h2,#app .sub,#app .hg>*,#app .form,#app .cw').forEach(function (el) {
      el.classList.add('rv');
      el.style.transitionDelay = Math.min(Array.prototype.indexOf.call(el.parentNode.children, el), 6) * 90 + 'ms';
      io.observe(el);
    });
  }

  // Video: bosilgandagina YouTube/Vimeo yuklanadi (sahifa tez ochiladi)
  $$('.vplay').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = b.dataset.embed; f.title = b.dataset.title || 'Video';
      f.allow = 'autoplay; encrypted-media; fullscreen; picture-in-picture';
      f.setAttribute('allowfullscreen', '');
      b.parentNode.replaceChild(f, b);
    });
  });

  // Galereya: rasmni kattalashtirib ko'rish
  var links = $$('a[data-lb]');
  if (links.length && window.HTMLDialogElement) {
    var dlg = document.createElement('dialog');
    dlg.className = 'lbx';
    dlg.innerHTML = '<img alt=""><button type="button" aria-label="' + esc(t('close', 'Yopish')) + '">×</button>';
    document.body.appendChild(dlg);
    var big = dlg.querySelector('img');
    dlg.querySelector('button').addEventListener('click', function () { dlg.close(); });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
    links.forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        big.src = a.href; big.alt = (a.querySelector('img') || {}).alt || '';
        dlg.showModal();
      });
    });
  }

  // Video va taqdimot oynasi (modal): kartochka bosilganda ochiladi, yopilganda video to'xtaydi
  var players = $$('[data-play]');
  if (players.length && window.HTMLDialogElement) {
    var pm = document.createElement('dialog');
    pm.className = 'pmodal';
    pm.innerHTML = '<div class="pm-box"><div class="pm-h"><b class="pm-t"></b><button type="button" class="pm-x" aria-label="' +
      esc(t('close', 'Yopish')) + '">×</button></div><div class="pm-f"></div></div>';
    document.body.appendChild(pm);
    var frame = pm.querySelector('.pm-f'), ttl = pm.querySelector('.pm-t');
    var stop = function () { frame.innerHTML = ''; };
    pm.querySelector('.pm-x').addEventListener('click', function () { pm.close(); });
    pm.addEventListener('click', function (e) { if (e.target === pm) pm.close(); });
    pm.addEventListener('close', stop);
    players.forEach(function (b) {
      b.addEventListener('click', function () {
        var mode = b.dataset.play, src = b.dataset.src;
        pm.className = 'pmodal ' + (mode === 'pdf' ? 'is-doc' : b.dataset.vertical === '1' ? 'is-v' : 'is-h');
        ttl.textContent = b.dataset.title || '';
        var el;
        if (mode === 'video') {
          el = document.createElement('video');
          el.src = src; el.controls = true; el.autoplay = true; el.setAttribute('playsinline', '');
        } else {
          el = document.createElement('iframe');
          el.src = src; el.title = b.dataset.title || 'Video';
          el.allow = 'autoplay; encrypted-media; fullscreen; picture-in-picture';
          el.setAttribute('allowfullscreen', '');
        }
        frame.innerHTML = ''; frame.appendChild(el);
        pm.showModal();
      });
    });
  }

  // Xizmatlar sahifasi: materiallarni xizmat bo'yicha saralash
  var chips = $$('.mfilter button');
  function applyFilter(f) {
    chips.forEach(function (c) { var on = c.dataset.f === f; c.classList.toggle('on', on); c.setAttribute('aria-pressed', on); });
    $$('[data-svc]').forEach(function (el) { el.hidden = !(f === 'all' || el.dataset.svc === f); });
  }
  chips.forEach(function (c) { c.addEventListener('click', function () { applyFilter(c.dataset.f); }); });
  $$('[data-goto]').forEach(function (a) {
    a.addEventListener('click', function () { if (chips.length) applyFilter(a.dataset.goto); });
  });

  // Ariza formalari
  function digits(v) { return String(v || '').replace(/\D/g, ''); }
  $$('form[data-lead]').forEach(function (form) {
    var msg = $('.fmsg', form), btn = $('button[type=submit]', form), label = btn.textContent;
    function say(text, ok) { msg.textContent = text; msg.className = 'fmsg ' + (ok ? 'ok' : 'err'); }
    function fieldError(input, text) { input.setAttribute('aria-invalid', 'true'); say(text); input.focus(); }

    // Xato tuzatilishi bilan qizil holat yo'qoladi
    form.addEventListener('input', function (e) {
      if (e.target.getAttribute('aria-invalid')) { e.target.removeAttribute('aria-invalid'); msg.textContent = ''; }
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.elements.name, phone = form.elements.phone;
      if (!name.value.trim()) return fieldError(name, t('name_err', 'Ismingizni yozing — kimga qo‘ng‘iroq qilishni bilishimiz uchun.'));
      if (digits(phone.value).length < 9) return fieldError(phone, t('phone_err', 'Telefon raqamini to‘liq yozing, masalan: 90 123-45-67.'));

      var data = {};
      Array.prototype.forEach.call(form.elements, function (el) { if (el.name) data[el.name] = el.value; });
      btn.disabled = true; btn.textContent = t('sending', 'Yuborilmoqda…'); msg.textContent = '';

      fetch('/api/lead', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok) throw new Error(res.j.error || '');
          form.innerHTML = '<div class="fdone"><b>' + esc(t('ok_title', 'Rahmat! Arizangiz qabul qilindi.')) + '</b><p>' + esc(t('ok_text', '1 ish kuni ichida siz bilan bog‘lanamiz.')) + '</p></div>';
        })
        .catch(function (err) {
          btn.disabled = false; btn.textContent = label;
          say(err.message || t('net_err', 'Ariza yuborilmadi — internet aloqasini tekshirib, qayta urinib ko‘ring.'));
        });
    });
  });
})();
