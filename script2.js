const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://studymalaysia.com/where/profile.php?code=mmu');
  const hrefElement = await page.$$('.resp-tab-item hor_1');
  await hrefElement[2].click();
  
  // ...
})();