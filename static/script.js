
document.addEventListener('DOMContentLoaded', function() {
    
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            updateProgress();
        });
    });
    
    
    const screenshotBtn = document.getElementById('screenshotBtn');
    if (screenshotBtn) {
        screenshotBtn.addEventListener('click', function() {
            alert('In a full version, this would generate an image of your learning path! For now, use print (Ctrl+P) or screenshot manually.');
        });
    }
});

function updateProgress() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const checked = Array.from(checkboxes).filter(cb => cb.checked).length;
    const total = checkboxes.length;
    const percentage = total > 0 ? Math.round((checked / total) * 100) : 0;
    
    
    console.log(`Progress: ${checked}/${total} (${percentage}%)`);
}