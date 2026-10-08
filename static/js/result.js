(function () {
    const resultCard = document.getElementById('resultCard');
    const resultActions = document.getElementById('resultActions');

    const stored = sessionStorage.getItem('result');

    if (!stored) {
        resultCard.innerHTML =
            '<div class="result-loading"><p>No result found. Please take the quiz first.</p>' +
            '<a href="/quiz" class="btn btn-primary" style="margin-top:1.5rem">Take the Quiz</a></div>';
        return;
    }

    const data = JSON.parse(stored);

    resultCard.innerHTML = `
        <div class="result-hero" style="background: linear-gradient(135deg, ${data.color}, ${data.color}dd);">
            <span class="result-hero-emoji">${data.emoji}</span>
            <h1>${data.name}</h1>
            <p>This is your predicted learning style</p>
        </div>
        <div class="result-body">
            <h2>What This Means</h2>
            <p class="result-explanation">${data.explanation}</p>
            <h2>Personalized Study Tips</h2>
            <ul class="result-tips">
                ${data.tips.map((tip) => `<li><span class="tip-check">✓</span><span>${tip}</span></li>`).join('')}
            </ul>
        </div>
        <div class="result-scores">
            <h3>Your Style Breakdown</h3>
            ${buildScoreBars(data.scores)}
        </div>
    `;

    resultActions.style.display = 'flex';

    setTimeout(() => animateScoreBars(data.scores), 100);

    function buildScoreBars(scores) {
        const labels = {
            visual: 'Visual',
            auditory: 'Auditory',
            reading: 'Reading',
            kinesthetic: 'Kinesthetic',
        };
        const colors = {
            visual: '#3b82f6',
            auditory: '#10b981',
            reading: '#f59e0b',
            kinesthetic: '#ef4444',
        };
        const total = Object.values(scores).reduce((a, b) => a + b, 0) || 1;

        return Object.keys(scores)
            .map((key) => {
                const pct = Math.round((scores[key] / total) * 100);
                return `
                    <div class="score-bar">
                        <span class="score-label">${labels[key]}</span>
                        <div class="score-track">
                            <div class="score-fill" data-width="${pct}" style="width:0%; background:${colors[key]};"></div>
                        </div>
                        <span class="score-value">${scores[key]}</span>
                    </div>
                `;
            })
            .join('');
    }

    function animateScoreBars(scores) {
        document.querySelectorAll('.score-fill').forEach((bar) => {
            bar.style.width = bar.dataset.width + '%';
        });
    }
})();
