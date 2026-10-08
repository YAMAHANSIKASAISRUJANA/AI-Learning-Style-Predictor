(function () {
    let currentQuestion = 0;
    let answers = new Array(QUESTIONS.length).fill(null);

    const questionNumberEl = document.getElementById('questionNumber');
    const questionTextEl = document.getElementById('questionText');
    const optionsContainer = document.getElementById('optionsContainer');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const quizCard = document.getElementById('quizCard');
    const quizLoading = document.getElementById('quizLoading');

    function renderQuestion() {
        const q = QUESTIONS[currentQuestion];
        questionNumberEl.textContent = `Question ${currentQuestion + 1}`;
        questionTextEl.textContent = q.text;

        optionsContainer.innerHTML = '';
        const letters = ['A', 'B', 'C', 'D'];

        q.options.forEach((opt, index) => {
            const btn = document.createElement('button');
            btn.className = 'quiz-option';
            if (answers[currentQuestion] === index) {
                btn.classList.add('selected');
            }
            btn.innerHTML = `
                <span class="option-marker">${letters[index]}</span>
                <span class="option-text">${opt.text}</span>
            `;
            btn.addEventListener('click', () => selectOption(index));
            optionsContainer.appendChild(btn);
        });

        const progress = ((currentQuestion + 1) / QUESTIONS.length) * 100;
        progressFill.style.width = progress + '%';
        progressText.textContent = `Question ${currentQuestion + 1} of ${QUESTIONS.length}`;

        prevBtn.disabled = currentQuestion === 0;
        nextBtn.textContent = currentQuestion === QUESTIONS.length - 1 ? 'See Results →' : 'Next →';
        nextBtn.disabled = answers[currentQuestion] === null;

        quizCard.style.animation = 'none';
        void quizCard.offsetHeight;
        quizCard.style.animation = 'fadeInUp 0.4s ease';
    }

    function selectOption(index) {
        answers[currentQuestion] = index;
        renderQuestion();
    }

    prevBtn.addEventListener('click', () => {
        if (currentQuestion > 0) {
            currentQuestion--;
            renderQuestion();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (answers[currentQuestion] === null) return;

        if (currentQuestion < QUESTIONS.length - 1) {
            currentQuestion++;
            renderQuestion();
        } else {
            submitQuiz();
        }
    });

    function submitQuiz() {
        quizCard.style.display = 'none';
        document.querySelector('.quiz-nav').style.display = 'none';
        document.querySelector('.quiz-progress-wrapper').style.display = 'none';
        quizLoading.style.display = 'block';

        fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ answers: answers }),
        })
            .then((res) => {
                if (!res.ok) throw new Error('Network response was not ok');
                return res.json();
            })
            .then((data) => {
                sessionStorage.setItem('result', JSON.stringify(data));
                window.location.href = '/result';
            })
            .catch((err) => {
                quizLoading.innerHTML =
                    '<p style="color:var(--error)">Something went wrong. Please try again.</p>';
                console.error(err);
            });
    }

    renderQuestion();
})();
