document.querySelectorAll('.tour-block-inner').forEach(function(block) {
    block.addEventListener('click', function(event) {

        event.preventDefault();
        
        var tourId = this.dataset.id; 
        window.location.href = `/tour-info/${tourId}/`;
    });
});