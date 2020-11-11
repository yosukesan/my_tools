#!/bin/bash

#declare DATA=`cat ecb_sample.data`
declare DATA=`curl -s https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html`
declare -A rates_in_EUR
declare -A converted_rates
declare arr_currs

function parse_html(){
    local currs=$(echo $DATA | grep -oE "<td id=\"[A-Z]*\" class=\"currency\">" | grep -oE "([A-Z]){3}")
    local rates=$(echo $DATA | grep -oE "<span class=\"rate\">[0-9]*\.[0-9]*<\/span><\/a>" | grep -oE "[0-9]*\.[0-9]*")

    arr_currs=($currs)
    local arr_rates=($rates)

    for i in $(seq 0 `expr ${#arr_rates[@]} - 1`); do
        #echo ${arr_currs[$i]} ${arr_rates[$i]}
        rates_in_EUR[${arr_currs[$i]}]+=${arr_rates[$i]}
    done
}

function base2A(){

    for i in $(seq 0 `expr ${#rates_in_EUR[@]} - 1`); do
        rate=`echo - | awk "{ print $1 / ${rates_in_EUR[${arr_currs[i]}]} }"`
        converted_rates[${arr_currs[i]}]+=$rate
    done
}

parse_html

# to JPY
base2A ${rates_in_EUR[JPY]} 

# to USD
#base2A ${rates_in_EUR[USD]} 

for i in $(seq 0 `expr ${#converted_rates[@]} - 1`); do
    echo ${arr_currs[$i]} ${converted_rates[${arr_currs[$i]}]}
done
