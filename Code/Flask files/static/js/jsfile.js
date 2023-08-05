function calculateBmi() {
var weight = document.bmiForm.pounds.value
var height = document.bmiForm.inches.value
if(weight > 0 && height > 0){	
var finalBmi = weight/(height/100*height/100)
document.bmiForm.bmi.value = finalBmi
    if(finalBmi < 18.5){
document.bmiForm.meaning.value = "Underweight"
}
if(finalBmi > 18.5 && finalBmi < 25){
document.bmiForm.meaning.value = "Normal"
}
if(finalBmi > 25){
document.bmiForm.meaning.value = "Overweight"
}
}
else{
alert("Please Fill in everything correctly")
}
}