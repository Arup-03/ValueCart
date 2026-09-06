async function compareProduct() {

    const input = document.getElementById("productUrl");
    const button = document.querySelector(".search-box button");

    const url = input.value.trim();

    if (!url) {
        alert("Please paste a product link first.");
        return;
    }

    button.textContent = "Comparing...";
    button.disabled = true;

    try {

        const response = await fetch("/compare", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                url: url
            })
        });


        const data = await response.json();

        console.log("ValueCart Result:", data);


        if (!response.ok || !data.success) {

            alert(
                data.error ||
                "Unable to compare prices."
            );

            return;
        }


        displayResults(data);

    }

    catch (error) {

        console.error(
            "ValueCart Error:",
            error
        );

        alert(
            "Unable to connect to ValueCart server."
        );

    }

    finally {

        button.textContent =
            "Compare Prices";

        button.disabled = false;
    }
}


/* =========================================
   DISPLAY RESULTS
========================================= */

function displayResults(data) {

    const results =
        document.getElementById("results");

    const bestPlatform =
        document.getElementById("bestPlatform");

    const bestPrice =
        document.getElementById("bestPrice");

    const saving =
        document.getElementById("saving");

    const priceList =
        document.getElementById("priceList");

    const resultTitle =
        document.getElementById("resultTitle");


    /* =========================================
       CHECK REQUIRED ELEMENTS
    ========================================= */

    if (
        !results ||
        !bestPlatform ||
        !bestPrice ||
        !saving ||
        !priceList
    ) {

        console.error(
            "ValueCart result elements not found."
        );

        return;
    }


    /* =========================================
       SHOW RESULTS
    ========================================= */

    results.classList.remove("hidden");


    /* =========================================
       BEST DEAL
    ========================================= */

    bestPlatform.textContent =
        data.best_deal.platform;


    bestPrice.textContent =
        "₹" +
        Number(
            data.best_deal.price
        ).toLocaleString("en-IN");


    /* =========================================
       SAVINGS
    ========================================= */

    const savings =
    Number(data.savings || 0);

saving.textContent =
    "Save ₹" +
    savings.toLocaleString("en-IN") +
    " compared with your current platform";

    /* =========================================
       PRODUCT NAME
    ========================================= */

    if (
        resultTitle &&
        data.best_deal.name
    ) {

        resultTitle.textContent =
            data.best_deal.name;
    }


    /* =========================================
       CLEAR OLD RESULTS
    ========================================= */

    priceList.innerHTML = "";


    /* =========================================
       PLATFORM LOGOS
    ========================================= */

    const platformLogos = {

        "Amazon":
            "/static/image/amazon.png",

        "Flipkart":
            "/static/image/flipkart.png",

        "Croma":
            "/static/image/croma.png",

        "Reliance Digital":
            "/static/image/reliance.png",

        "Tata CLiQ":
            "/static/image/tatacliq.png"

    };


    /* =========================================
       CREATE PRICE CARDS
    ========================================= */

    data.comparison.forEach(item => {

        const card =
            document.createElement("div");


        card.className =
            "price-card";


        /* =====================================
           HIGHLIGHT BEST DEAL
        ===================================== */

        if (
            item.platform ===
            data.best_deal.platform
        ) {

            card.classList.add("best");
        }


        /* =====================================
           GET PLATFORM LOGO
        ===================================== */

        const logo =
            platformLogos[item.platform] ||
            "";


        /* =====================================
           CARD HTML
        ===================================== */

        card.innerHTML = `

            <div class="platform-info">

                <img
                    src="${logo}"
                    alt="${item.platform} logo"
                    class="platform-logo"
                >

                <div class="platform-name">

                    <span>
                        ${item.platform}
                    </span>

                    <small>
                        Available price
                    </small>

                </div>

            </div>


            <div class="platform-price">

                ₹${Number(item.price)
                    .toLocaleString("en-IN")}

            </div>


            <a
                href="${item.url}"
                target="_blank"
                rel="noopener noreferrer"
                class="view-deal"
            >
                View Deal →
            </a>

        `;


        /* =====================================
           ADD CARD TO PAGE
        ===================================== */

        priceList.appendChild(card);

    });


    /* =========================================
       SCROLL TO RESULTS
    ========================================= */

    results.scrollIntoView({

        behavior: "smooth",

        block: "start"

    });

}