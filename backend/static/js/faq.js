document.addEventListener('DOMContentLoaded', () => {
    const questions = document.querySelectorAll('.faq-question');

    questions.forEach(question => {
        question.addEventListener('click', () => {
            // Toggle active class on the clicked question
            question.classList.toggle('active');

            // Toggle active class on the answer
            const answer = question.nextElementSibling;
            answer.classList.toggle('active');

            // Close other answers
            questions.forEach(q => {
                if (q !== question) {
                    q.classList.remove('active');
                    q.nextElementSibling.classList.remove('active');
                }
            });
        });
    });
});
