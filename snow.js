
(function () {
    // 1. Inject CSS for snowflakes
    const style = document.createElement('style');
    style.innerHTML = `
        .snowflake {
            position: fixed;
            top: -10px;
            background-color: #fff; /* White dots */
            border-radius: 50%;     /* Round shape */
            pointer-events: none;   /* Click-through */
            z-index: 9999;
            will-change: transform;
            animation-name: fall, sway;
            animation-timing-function: linear, ease-in-out;
            animation-iteration-count: 1, infinite;
            box-shadow: 0 0 2px rgba(255,255,255,0.8); /* Soft glow */
        }

        @keyframes fall {
            0% { top: -10px; opacity: 1; }
            100% { top: 100vh; opacity: 0; }
        }

        @keyframes sway {
            0% { transform: translateX(0); }
            50% { transform: translateX(25px); }
            100% { transform: translateX(0); }
        }
    `;
    document.head.appendChild(style);

    // 2. Snow Logic
    let isSnowing = false;
    let snowInterval = null;

    function createSnowflake() {
        if (!isSnowing) return;

        const snowflake = document.createElement('div');
        snowflake.classList.add('snowflake');

        // Random horizontal position
        snowflake.style.left = Math.random() * 100 + 'vw';

        // Random size (small dots)
        const size = Math.random() * 3 + 2 + 'px'; // 2px to 5px
        snowflake.style.width = size;
        snowflake.style.height = size;

        // Random animation duration (Very slow falling)
        // 10s to 20s fall time
        const fallDuration = Math.random() * 10 + 10 + 's';

        // Random sway duration
        const swayDuration = Math.random() * 4 + 3 + 's';

        snowflake.style.animationDuration = `${fallDuration}, ${swayDuration}`;
        snowflake.style.opacity = Math.random() * 0.2 + 0.8; // 0.8 to 1.0 opacity (Solid White)

        document.body.appendChild(snowflake);

        // Remove after animation finishes
        setTimeout(() => {
            snowflake.remove();
        }, parseFloat(fallDuration) * 1000);
    }

    function startSnowing() {
        isSnowing = true;
        // Create a snowflake every 150ms
        snowInterval = setInterval(createSnowflake, 150);
    }

    function stopSnowing() {
        isSnowing = false;
        clearInterval(snowInterval);
    }

    function runCycle() {
        console.log("Snow cycle: START (5s)");
        startSnowing();

        setTimeout(() => {
            console.log("Snow cycle: STOP (Wait 60s)");
            stopSnowing();

            setTimeout(runCycle, 60000); // Wait 60s (1 min) then restart
        }, 5000); // Run for 5s
    }

    // Start the loop
    runCycle();

})();
