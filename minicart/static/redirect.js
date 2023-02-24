import STRIPE_PUBLIC_KEY from './config.js';

const stripe = Stripe(STRIPE_PUBLIC_KEY);

const buyButton = document.querySelector('#buy-button');
buyButton.addEventListener('click', redirectToCheckout);

function redirectToCheckout() {
    const itemIndex = getItemIndex();
    const href = `/buy/${itemIndex}`;

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

function getItemIndex() {
    const pathname = window.location.pathname;
    const pattern = /^\/item\/(?<itemIndex>[0-9]+)$/;
    const { groups: { itemIndex } } = pattern.exec(pathname);
    return itemIndex;
} 