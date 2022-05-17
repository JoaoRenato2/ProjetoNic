let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");
let searchBtn = document.querySelector(".bx-search");
let content = getDatesBetween("2022/01/01", "2023/01/01");
document.getElementById("calendar").innerHTML = content;

btn.onclick = function () {
    sidebar.classList.toggle("active");
}

searchBtn.onclick = function () {
    sidebar.classList.toggle("active");
}

function getDatesBetween(date1, date2) {
    let reange1 = new Date(date1);
    let reange2 = new Date(date2);
    date1 = settingDate(date1, 31);
    date2 = settingDate(date2, 31);
    let temp;
    let dates = [];
    while (date1 <= date2) {
        if (date1.getDate() != 31) {
            temp = settingDate(date1, 0);
            if (temp >= reange1 && temp <= reange2) {
                dates.push(temp);
            }
            date1 = settingDate(date1, 31);
        } else {
            temp = new Date(date1);
            if (temp >= reange1 && temp <= reange2) dates.push(temp);
            date1.setMonth(date1.getMonth() + 1)
        }
    }

    let content = "";
    let weekDays = [{
        shortDay: "Seg",
        fullDay: "Segunda"
    }, {
        shortDay: "Ter",
        fullDay: "Terça"
    }, {
        shortDay: "Qua",
        fullDay: "Quarta"
    }, {
        shortDay: "Qui",
        fullDay: "Quinta"
    }, {
        shortDay: "Sex",
        fullDay: "Sexta"
    }, {
        shortDay: "Sab",
        fullDay: "Sabado"
    }, {
        shortDay: "Dom",
        fullDay: "Domingo"
    }];
    let LastDate, firstDate;
    for (let i = 0; i < dates.length; i++) {
        LastDate = dates[i];
        firstDate = new Date(dates[i].getFullYear(), dates[i].getMonth(), 1);
        content += "<div id='calendar_Table" + (i + 1) + "'>";
        content += "<h2>" +
            firstDate.toString().split(" ")[1] + "-" +
            firstDate.getFullYear() +
            "</h2>";
        content += "<table >";
        content += "<thead >";
        weekDays.map(item => {
            content += "<th>" + item.fullDay + "</th>";
        });
        content += "</thead >";
        content += "<tbody >";
        let j = 1;
        let displaynum, idMonth;
        while (j <= LastDate.getDate()) {
            content += "<tr>";
            for (let k = 0; k < 7; k++) {
                displaynum = j < 10 ? "0" + j : j;
                if (j == 1) {
                    if (firstDate.toString().split(" ")[0] == weekDays[k].shortDay) {
                        content += "<td>" + displaynum + "</td>";
                        j++;
                    } else {
                        content += "<td></td>";

                    }
                } else {
                    if (j > LastDate.getDate()) {
                        content += "<td></td>";

                    } else {
                        content += "<td>" + displaynum + "</td>";
                        j++;
                    }
                }
            }
            content += "</tr>";

        }
        content += "</tbody >";
        content += "</table >";
        content += "</div>";
    }

    return content;

}

function settingDate(date, day) {
    date = new Date(date);
    date.setDate(day);
    date.setHours(23);
    return date;
}