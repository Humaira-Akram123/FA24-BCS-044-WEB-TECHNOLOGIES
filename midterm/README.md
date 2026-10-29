# Midterm — Aven Perfumes (built on my Assignment 2 page)

| | |
|---|---|
| **Name** | YOUR NAME HERE |
| **Roll / Reg. number** | FA24-BCS-044 |
| **N** | 44 |
| **BP** | 992 px |
| **H** | (not used by my tasks) |
| **K** | 4 columns / groups |
| **Exam date used for min/max** | 2026-10-29 (max = +44 days = 2026-12-12) |

> The N, BP, H, K and exam-date values above are the ones I used. If my exam sheet says otherwise, they are one-line changes (see "Where to change things").

## Files changed
- `index.html` — mega-menu + mobile accordion in the navbar, cart badge/mini-cart markup, "Add to Cart" buttons, `<script src="script.js">`; fixed broken tags (stray `<`, missing brand `<a>`, `</>`) and removed a stray product-description block that had been pasted into the footer.
- `styles.css` — new sections for Task 1, Task 2, Task 3 (at the end of the file); `hero.jpg` -> `Hero.jpg` (file name case).
- `checkout.html` — **new** (Task 2).
- `script.js` — **new** (Task 3).
- `README.md`, `FA24-BCS-044-midterm.pdf`.

## Task 1 — Mega-menu
- Added a "Shop by Category" item to the existing navbar. From 992px up, `.mega:hover > .mega-panel, .mega:focus-within > .mega-panel { display:block }` opens a full-width panel (4 `<section>` columns, each with an `<h3>` and a `<ul>` of 5 links). `:focus-within` makes it open with Tab alone and close when focus leaves.
- The panel is `position:absolute; top:100%; left:0; right:0` inside the (already absolutely positioned) navbar, so it overlays the page without pushing content, and the navbar has `z-index:2000` so it is above the grid, cards and the fixed back-to-top button. The menu item gets `padding-bottom:60px; margin-bottom:-60px` so the pointer stays "inside" it while travelling into the panel.
- Below 992px the panel is hidden and the same 4 groups appear inside the hamburger menu as `<details>/<summary>` (closed by default, each independent). No JavaScript of mine is used.

## Task 2 — Checkout form
- `checkout.html` (linked from the cart icon): two `<fieldset>`/`<legend>` groups (Contact, Delivery), every input has `<label for>`/`id`. Phone uses `pattern="03[0-9]{2}-[0-9]{7}"`; date uses `min="2026-10-29" max="2026-12-12"`; city is a `<select>` with an empty required first option.
- Errors: `input:user-invalid` gives the red border and reveals the sibling `.msg` — so nothing shows on page load, only after interaction.
- Layout: CSS Grid. From 992px the form is 2 columns (fieldsets side by side) and each fieldset is `110px 1fr` (labels left); below that everything is one column with labels above inputs. Submit button is `width:100%` always.

## Task 3 — Cart (script.js)
- Each product card now has an "Add to Cart" button (cards changed from `<a>` to `<article>` because a button must not sit inside a link). Click reads name and price from the card and pushes `{name, price}` into the `cart` array; `render()` redraws the badge, the list and the total.
- The cart icon toggles the mini-cart (`preventDefault`; without JS it just goes to checkout.html, and the panel also has a Checkout link). Total uses `cart.reduce(...)`. "Remove" deletes that entry and re-renders immediately.
- `MAX_PER_PRODUCT = (N % 4) + 2` = 2. When a product reaches it the button says "Limit reached" and is disabled; removing one re-enables it.

## Where to change things
- BP: the `992px` / `991.98px` media queries in `styles.css` **and** `navbar-expand-lg` on the `<nav>` in `index.html`.
- K (columns): `repeat(4, 1fr)` in `.mega-cols`, plus add/remove `<section class="mega-col">` and `<details>` groups.
- N / limit: `const N` in `script.js`. Date window: `min`/`max` on `#date`.

## AI tools used
Claude (Anthropic) — used to help write and test the code; I reviewed and can explain all of it.
