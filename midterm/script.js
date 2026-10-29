/* MIDTERM TASK 3 — cart badge + mini cart (plain JavaScript) */

const N = 44;                                // my number from the exam sheet
const MAX_PER_PRODUCT = (N % 4) + 2;         // a product can be added at most this many times

let cart = [];                               // array of { name, price }

const badge     = document.getElementById('cartBadge');
const cartBtn   = document.getElementById('cartBtn');
const miniCart  = document.getElementById('miniCart');
const listEl    = document.getElementById('miniCartList');
const emptyEl   = document.getElementById('miniEmpty');
const totalEl   = document.getElementById('miniTotal');
const cards     = document.querySelectorAll('.product-card');

// "Rs.2,400.00 PKR" -> 2400
function parsePrice(text) {
  const match = text.match(/\d[\d,]*\.?\d*/);
  return match ? parseFloat(match[0].replace(/,/g, '')) : 0;
}
function formatRs(n) {
  return 'Rs.' + n.toLocaleString('en-PK', { minimumFractionDigits: 0, maximumFractionDigits: 2 });
}
function countOf(name) {
  return cart.filter(item => item.name === name).length;
}

// refresh every part of the UI from the cart array
function render() {
  // badge
  badge.textContent = cart.length;
  badge.hidden = cart.length === 0;

  // mini cart list
  listEl.textContent = '';
  cart.forEach((item, index) => {
    const li = document.createElement('li');

    const name = document.createElement('span');
    name.className = 'mi-name';
    name.textContent = item.name;

    const price = document.createElement('span');
    price.className = 'mi-price';
    price.textContent = formatRs(item.price);

    const remove = document.createElement('button');
    remove.type = 'button';
    remove.className = 'mi-remove';
    remove.textContent = 'Remove';
    remove.dataset.index = index;

    li.append(name, price, remove);
    listEl.appendChild(li);
  });
  emptyEl.hidden = cart.length > 0;

  // total with reduce()
  const total = cart.reduce((sum, item) => sum + item.price, 0);
  totalEl.textContent = formatRs(total);

  // Add to Cart buttons: limit reached?
  cards.forEach(card => {
    const btn = card.querySelector('.btn-add');
    const name = card.querySelector('.product-name').textContent.trim();
    const reached = countOf(name) >= MAX_PER_PRODUCT;
    btn.disabled = reached;
    btn.textContent = reached ? 'Limit reached' : 'Add to Cart';
  });
}

// Add to Cart (name and price are read from the card itself)
cards.forEach(card => {
  card.querySelector('.btn-add').addEventListener('click', () => {
    const name  = card.querySelector('.product-name').textContent.trim();
    const price = parsePrice(card.querySelector('.price:not(.price-old)').textContent);
    if (countOf(name) >= MAX_PER_PRODUCT) return;
    cart.push({ name, price });
    render();
  });
});

// Remove button (event delegation)
listEl.addEventListener('click', e => {
  const btn = e.target.closest('.mi-remove');
  if (!btn) return;
  cart.splice(Number(btn.dataset.index), 1);
  render();
});

// cart icon toggles the mini cart (without JS it simply links to checkout.html)
cartBtn.addEventListener('click', e => {
  e.preventDefault();
  const open = miniCart.hidden;             // currently closed -> open it
  miniCart.hidden = !open;
  cartBtn.setAttribute('aria-expanded', String(open));
});

render();
