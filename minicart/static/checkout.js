import STRIPE_PUBLIC_KEY from './config.js';

const stripe = Stripe(STRIPE_PUBLIC_KEY);

addOnClickEvents();

function addOnClickEvents() {
    const buyButton = document.querySelector('#buy-button');
    const addToOrderButton = document.querySelector('#add-to-order-button');
    const orderButton = document.querySelector('#order-button')

    buyButton?.addEventListener('click', () => {
        const itemIndex = getItemIndex();
        const href = `/buy/${itemIndex}`;
        createCheckoutSessionAndRedirect(href);
    });
    addToOrderButton?.addEventListener('click', addToCart);
    orderButton?.addEventListener('click', () => {
        const href = '/order';
        createCheckoutSessionAndRedirect(href);
    });
}

function createCheckoutSessionAndRedirect(href) {
    // Create a new Checkout Session using the server-side endpoint 
    // Redirect to Stripe Session Checkout
    fetch(href, { method: 'GET' })
        .then(response => response.json())
        .then(session => stripe.redirectToCheckout({ 
            sessionId: session.id
        }))
        .then(result => {
            if (result.error)
                alert(result.error.message);
        })
        .catch(error => {
            console.error('Error:', error)
        });
}

function addToCart() {
    const itemIndex = getItemIndex();
    const href = `/cart/add/${itemIndex}`;
    
    fetch(href, { method: 'GET' })
        .then(result => {
            if (result.ok)
                alert('Item added successfully to your cart!');
            else if (result.error)
                alert(result.error.message);
        })
        .catch(error => {
            console.error('Error:', error)
        });
}

function getItemIndex() {
    const pathname = window.location.pathname;
    const pattern = /^\/item\/(?<itemIndex>[0-9]+)$/;
    const { groups: { itemIndex } } = pattern.exec(pathname);
    return itemIndex;
} 