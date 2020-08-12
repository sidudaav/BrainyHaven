$(window).scroll(function () {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $('section.counters').offset().top;
    var elemBottom = elemTop + $('section.counters').height();

    if ((elemBottom <= docViewBottom) && (elemTop >= docViewTop)) {
        const counters = document.querySelectorAll('.counter');
        const speed = 500; // The lower the slower

        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;

                // Lower inc to slow and higher to slow
                const inc = target / speed;

                // console.log(inc);
                // console.log(count);

                // Check if target is reached
                if (count < target) {
                    // Add inc to count and output in counter
                    counter.innerText = count + inc;
                    // Call function every ms
                    setTimeout(updateCount, 1);
                } else {
                    counter.innerText = target.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");;
                }
            };

            updateCount();
        });
    }
});