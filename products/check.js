// node check.js in.html  -> reports pages whose content runs into the footer area
const { chromium } = require(process.env.PW_PATH || 'playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 816, height: 1056 } });
  await p.goto('file://' + process.argv[2]); await p.waitForTimeout(400);
  const res = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
    const top = pg.getBoundingClientRect().top; let max = 0;
    pg.querySelectorAll(':scope > *:not(.run):not(.foot)').forEach(e => { max = Math.max(max, e.getBoundingClientRect().bottom - top); });
    return [i + 1, Math.round(max)];
  }));
  res.forEach(([n, m]) => { if (m > 985) console.log('OVERFLOW page', n, 'content bottom', m, '(limit ~985)'); });
  console.log('checked', res.length, 'pages'); await b.close();
})();
