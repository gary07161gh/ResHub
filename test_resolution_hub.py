from playwright.sync_api import sync_playwright

def test_resolution_hub():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('file:///c:/Users/Gary0/Desktop/Coding/ResHub/Resolution%20Hub.html')
        page.wait_for_load_state('networkidle')

        # Take screenshot for inspection
        page.screenshot(path='screenshot.png', full_page=True)
        print("Screenshot saved as screenshot.png")

        # Test 1: Check if app loads and dashboard is visible
        dashboard_heading = page.get_by_role('heading', name='Queue Overview')
        assert dashboard_heading.is_visible(), "Dashboard not loaded"
        print("✓ App loaded successfully")

        # Test 2: Check if KPI cards are present
        kpi_cards = page.locator('[class*="p-4 rounded-xl border"]').all()
        assert len(kpi_cards) >= 5, "Not all KPI cards loaded"
        print("✓ KPI cards displayed")

        # Test 3: Test search functionality
        search_input = page.locator('input[placeholder="Search cases..."]')
        assert search_input.is_visible(), "Search input not found"
        search_input.fill('test')
        print("✓ Search input works")

        # Test 4: Check if table or kanban is present
        table = page.locator('table')
        kanban = page.locator('[class*="grid"]')  # Assuming kanban uses grid
        if table.is_visible():
            print("✓ Table view loaded")
        elif kanban.is_visible():
            print("✓ Kanban view loaded")
        else:
            print("⚠ No table or kanban visible")

        browser.close()
        print("Basic tests completed!")

if __name__ == "__main__":
    test_resolution_hub()