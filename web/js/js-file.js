
function updateText(text) {
    const tAussenAct = document.getElementById("tAussenAct");
    tAussenAct.innerHTML = text;
}

function startApp() {
    eel.startApp();
}

function stopApp() {
    eel.stopApp();
}

function setResolution(width, height) {
    eel.setResolution(width, height)
}

eel.expose(updateTime)
function updateTime(timestring) {
    const titleHead = document.getElementById("titleHead");
    titleHead.innerHTML = timestring

}

eel.expose(update_values); // Expose this function to Python
function update_values(name, temperature, humidity, battery, timeout) {
    const elem = document.getElementById(name);
    const divSensors = document.getElementById("divSensors");
    if (elem == null) {
        var divSensor = document.createElement("div");
        divSensor.className = "divSensor";
        divSensors.appendChild(divSensor);
        var tagName = document.createElement("h4");
        tagName.id = name;
        tagName.innerHTML = name;
        tagName.className = "sensorName";
        console.log(tagName)
        divSensor.appendChild(tagName);

        var section1 = document.createElement("section");
        section1.className="inlineFlex";
        divSensor.appendChild(section1);
        
        var tagTemp = document.createElement("h5");
        tagTemp.id = name + "Temp";
        tagTemp.innerHTML = temperature + " °C";
        tagTemp.className = "sensorValue";
        section1.appendChild(tagTemp);

        var img_reload = document.createElement("img");
        img_reload.src="images/history_FILL0_wght400_GRAD0_opsz48.svg";
        img_reload.id=name +"ind_timeout";
        img_reload.style.display="none";
        section1.appendChild(img_reload)



        var section2 = document.createElement("section");
        section2.className="inlineFlex";
        divSensor.appendChild(section2);
        
        var tagHum = document.createElement("h5");
        tagHum.id = name + "Hum";
        tagHum.innerHTML = humidity + " %";
        tagHum.className = "sensorValue";
        section2.appendChild(tagHum);

        var img_weak_bat = document.createElement("img");
        img_weak_bat.src="images/battery_low_FILL0_wght400_GRAD0_opsz48.svg";
        img_weak_bat.id=name +"ind_battery_weak";
        img_weak_bat.style.display="none";
        section2.appendChild(img_weak_bat)

        var img_empty_bat = document.createElement("img");
        img_empty_bat.src="images/battery_very_low_FILL0_wght400_GRAD0_opsz48.svg";
        img_empty_bat.id=name +"ind_battery_empty";
        img_empty_bat.style.display="none";
        section2.appendChild(img_empty_bat)
        
    }
    else {
        //console.log(`bekannter sensor : ${name} `);
        const tempValue = document.getElementById(name + "Temp");
        tempValue.innerHTML = temperature + " °C";
        const humValue = document.getElementById(name + "Hum");
        humValue.innerHTML = humidity + " %";

        const ind_battery_empty = document.getElementById(name+"ind_battery_empty");
        const ind_battery_weak = document.getElementById(name+"ind_battery_weak");
           
        if (battery < 25) { 
            ind_battery_empty.style.display="inline";
        }
        else if (battery < 10) { 
            ind_battery_weak.style.display="inline";
        }
        else{
            ind_battery_empty.style.display="none";
            ind_battery_weak.style.display="none";
        }
        const ind_timeout = document.getElementById(name+"ind_timeout");      
        if (timeout > 100) {
            ind_timeout.style.display="inline";
        }
        else{
            ind_timeout.style.display="none";
        }
    }
}

eel.say_hello_py("Javascript World!"); // Call a Python function