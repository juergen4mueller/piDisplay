
eel.expose(updateTime)
function updateTime(timestring) {
    const titleHead = document.getElementById("titleHead");
    titleHead.innerHTML = timestring
}

eel.expose(update_home_sensors); // Expose this function to Python
function update_home_sensors(name, temperature, humidity, battery, timeout) {
  
}

eel.expose(update_weather_data); // Expose this function to Python
function update_weather_data(i, time, temperature_2m_min, temperature_2m_max, sunrise, sunset, rain_sum, windspeed_10m_max, windgusts_10m_max, winddirection_10m_dominant, shortwave_radiation_sum)
{

}


eel.expose(update_holfuy_data); // Expose this function to Python
function update_holfuy_data(name, updateTime, wSpeed, wGust, wMin, wUnit, wDirection, pressure, temperature)
{          
    
    
    if(name == "Oberemmendorf"){
        const nameOE = document.getElementById("nameOE"); 
        nameOE.innerHTML= name;
        const updateTimeOE = document.getElementById("updateTimeOE"); 
        updateTimeOE.innerHTML= updateTime;
        const wMinOE = document.getElementById("wMinOE") ;
        wMinOE.innerHTML= wMin +" "+wUnit;
        const wSpeedOE = document.getElementById("wSpeedOE");
        wSpeedOE.innerHTML= wSpeed +" "+wUnit;
        const wGustOE = document.getElementById("wGustOE");
        wGustOE.innerHTML = wGust +" "+wUnit;
        const wDirectionOE = document.getElementById("wDirectionOE");
        wDirectionOE.innerHTML = wDirection;
        const pressureOE = document.getElementById("pressureOE");
        pressureOE.innerHTML = pressure;
        const temperatureOE = document.getElementById("temperatureOE");
        temperatureOE.innerHTML = temperature+" °C";
        // color wind speed
        if((wSpeed>=10)&&(wSpeed<15)){wSpeedOE.style.backgroundColor="green";}
        else if((wSpeed>=15)&&(wSpeed<20)){wSpeedOE.style.backgroundColor="orange"}
        else if(wSpeed>=20){wSpeedOE.style.backgroundColor="red"}
        // color gust speed
        if((wGust>=15)&&(wGust<25)){wGustOE.style.backgroundColor="green"}
        else if((wGust>=25)&&(wGust<35)){wGustOE.style.backgroundColor="orange"}
        else if(wGust>=35){wGustOE.style.backgroundColor="red"}
        if((wDirection>290)||(wDirection<20)){
            wDirectionOE.style.backgroundColor="green";
        }
        else if((wDirection>270)||(wDirection<40)){
            wDirectionOE.style.backgroundColor="orange";
        }
    }
    if(name == "Böhming"){
        const nameBO = document.getElementById("nameBO");
        nameBO.innerHTML = name;
        const updateTimeBO = document.getElementById("updateTimeBO");
        updateTimeBO.innerHTML = updateTime;
        const wMinBO = document.getElementById("wMinBO");
        wMinBO.innerHTML = wMin +" "+wUnit;
        const wSpeedBO = document.getElementById("wSpeedBO");
        wSpeedBO.innerHTML = wSpeed +" "+wUnit;
        const wGustBO = document.getElementById("wGustBO");
        wGustBO.innerHTML = wGust +" "+wUnit;
        const wDirectionBO = document.getElementById("wDirectionBO");
        wDirectionBO.innerHTML = wDirection;
        const pressureBO = document.getElementById("pressureBO");
        pressureBO.innerHTML = pressure;
        const temperatureBO = document.getElementById("temperatureBO");
        temperatureBO.innerHTML = temperature+" °C";
        // color wind speed
        if((wSpeed>=10)&&(wSpeed<15)){wSpeedBO.style.backgroundColor="green"}
        else if((wSpeed>=15)&&(wSpeed<20)){wSpeedBO.style.backgroundColor="orange"}
        else if(wSpeed>=20){wSpeedBO.style.backgroundColor="red"}
        // color gust speed
        if((wGust>=15)&&(wGust<25)){wGustBO.style.backgroundColor="green"}
        else if((wGust>=25)&&(wGust<35)){wGustBO.style.backgroundColor="orange"}
        else if(wGust>=35){wGustBO.style.backgroundColor="red"}
        if((wDirection>65)||(wDirection<145)){
            wDirectionBO.style.backgroundColor="green";
        }
        else if((wDirection>45)||(wDirection<170)){
            wDirectionBO.style.backgroundColor="orange";
        }
    }
    
    if(name == "Schernfeld"){
        const nameSF = document.getElementById("nameSF");
        nameSF.innerHTML = name;
        const updateTimeSF = document.getElementById("updateTimeSF");
        updateTimeSF.innerHTML = updateTime;
        const wMinSF = document.getElementById("wMinSF");
        wMinSF.innerHTML = wMin +" "+wUnit;
        const wSpeedSF = document.getElementById("wSpeedSF");
        wSpeedSF.innerHTML = wSpeed +" "+wUnit;
        const wGustSF = document.getElementById("wGustSF");
        wGustSF.innerHTML = wGust +" "+wUnit;
        const wDirectionSF = document.getElementById("wDirectionSF");
        wDirectionSF.innerHTML = wDirection;
        const pressureSF = document.getElementById("pressureSF");
        pressureSF.innerHTML = pressure;
        const temperatureSF = document.getElementById("temperatureSF");
        temperatureSF.innerHTML = temperature+" °C";
        // color wind speed
        if((wSpeed>=10)&&(wSpeed<15)){wSpeedSF.style.backgroundColor="green"}
        else if((wSpeed>=15)&&(wSpeed<20)){wSpeedSF.style.backgroundColor="orange"}
        else if(wSpeed>=20){wSpeedSF.style.backgroundColor="red"}
        // color gust speed
        if((wGust>=15)&&(wGust<25)){wGustSF.style.backgroundColor="green"}
        else if((wGust>=25)&&(wGust<35)){wGustSF.style.backgroundColor="orange"}
        else if(wGust>=35){wGustSF.style.backgroundColor="red"}
        // color wind direction
        if((wDirection>190)||(wDirection<250)){wDirectionSF.style.backgroundColor="green";}
        else if((wDirection>170)||(wDirection<290)){wDirectionSF.style.backgroundColor="orange";}

    }

}

eel.request_data("flugwetter"); // aktive anfrage der Daten bei Start oder Seitenwechsel, Init-Page = 0