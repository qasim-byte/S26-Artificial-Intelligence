document.getElementById("gpaForm").addEventListener("submit", function (e) {

    let valid = true;
    let messages = [];

    const fields = [
        {name: "Age", min: 10, max: 25},
        {name: "Ethnicity", min: 0, max: 3},
        {name: "ParentalEducation", min: 0, max: 4},
        {name: "StudyTimeWeekly", min: 0, max: 50},
        {name: "Absences", min: 0, max: 100},
        {name: "ParentalSupport", min: 0, max: 4},
        {name: "GradeClass", min: 1, max: 12}
    ];

    fields.forEach(f => {
        let input = document.querySelector(`[name="${f.name}"]`);
        let value = Number(input.value);

        if (value < f.min || value > f.max) {
            valid = false;
            input.classList.add("error");
            messages.push(`${f.name} must be between ${f.min} and ${f.max}`);
        } else {
            input.classList.remove("error");
        }
    });

    if (!valid) {
        e.preventDefault();
        alert(messages.join("\n"));
    }
});