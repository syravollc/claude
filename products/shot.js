// node shot.js in.html outdir prefix  -> one PNG per .page
const { chromium } = require(process.env.PW_PATH || 'playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 0.7 });
  await p.goto('file://' + process.argv[2]); await p.waitForTimeout(500);
  const els = await p.$$('.page'); let i = 0;
  for (const e of els) { await e.screenshot({ path: `${process.argv[3]}/${process.argv[4]}-${String(i++).padStart(2, '0')}.png` }); }
  console.log(els.length + ' pages'); await b.close();
})();
