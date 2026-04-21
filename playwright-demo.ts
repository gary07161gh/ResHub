import { test } from '@playwright/test';

test('demo playwright mcp capabilities', async ({ page }) => {
  await page.goto('https://example.com');
  console.log(await page.title());
  await page.screenshot({ path: 'example.png' });
});

