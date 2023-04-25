 //1
// age = prompt('Введите ваш возраст')
// function whoAreYou(age) {
//     if(age>=0&&age<3) log('you are child') 
//     else if(age>=12&&age<19) log('you are teenager')
//     else if(age>18&&age<61) log('you are adult')
//     else if(age>60) log('you are pensioner')
// }
// whoAreYou(age)
//2
// function specialCharacter() {
//    let numbers = prompt('Введите от 0 до 9');
//    let valid = /^[0-9]+$/g;
//    if(numbers == 0){
//        alert(')')
//    }else if (numbers == 1){
//        alert('!')
//    }else if  (numbers == 2){
//        alert('@')
//    }else if  (numbers == 3){
//        alert('#')
//    }else if  (numbers == 4){
//        alert('$')
//    }else if  (numbers == 5){
//        alert('%')
//    }else if  (numbers == 6){
//        alert('^')
//    }else if  (numbers == 7){
//        alert('&')
//    }else if  (numbers == 8){
//        alert('*')
//    }else if  (numbers == 9){
//        alert('(')
//    }else if  (numbers > 9){
//        alert('Больше 9 вводить нельзя !')
//    }else if (valid.test(numbers)){
//    }else{
//        alert('Строки запрещены !')
//    }
// }
// specialCharacter()
//3
// const checkStr = (str) => {
//    if(!str) return alert("Нет строки")
//    str.replace(/[^+\d]/g, '')
//    if(str.length !== 3) return alert("Число должно быть трёхзначным")
//    let arr = str.split("")
//    let arrScanned = []
//    for(let i = 0; i < arr.length; i++){
//      if(arrScanned.indexOf(arr[i]) !== -1){
//        return true
//      }
//      arrScanned.push(arr[i])
//    }
//    return false
//  }
//  let str = prompt("Введите трёхзначное число")
//  console.log(checkStr(str))
//4
//  function leapYear(year){
//    if((year%4==0) && (year%100 !==0) || (year%400==0)){
//        return true;
//    }
//    else{
//        return false;
//    }
// }
// var result = leapYear(1700);
// console.log(result);
//5
// function palindrome(x) {
//    // если перед нами ноль — это палиндром
//    if(x == 0) {
//        return true;
//    }
//    // если число меньше нуля или делится на 10 без остатка — это не палиндром
//    if(x < 0 || x%10 == 0){
//        return false;
//    }
//6
    // let usd=parseInt(prompt('Enter amount of usd: '));
    // let type=parseInt(prompt('Enter currency you want to convert: 1 - eur, 2 - uan, 3 - azn: '));
    // switch (type){
    //     case 1:
    //         console.log(`eur - ${usd*0.89}`);
    //         break;
    //     case 2:
    //         console.log(`uan - ${usd*25.83}`);
    //         break;
    //     case 3:
    //         console.log(`azn - ${usd*1.7}`);
    //         break;
    // }

//7
    // let sumSale=parseInt(prompt('Enter sum of your purchare: '));
    // if(sumSale>=200&&sumSale<300){
    //     console.log(`your discount: 3%. For payment - ${sumSale*0.97}`);
    // }else if(sumSale>=300&&sumSale<500) {
    //     console.log(`your discount: 5%. For payment - ${sumSale*0.95}`);
    // }else if(sumSale>=500){
    //     console.log(`your discount: 7%. For payment - ${sumSale*0.93}`);
    // }

//8
    // let lengthOfCircle=parseInt(prompt('Enter a length of circle: '));
    // let perimeterOfSquare=parseInt(prompt('Enter a perimeter of square: '));
    // if(perimeterOfSquare/4>lengthOfCircle/Math.PI) {
    //     console.log('Circle is placed into square');
    // }else{
    //     console.log('Circle is not placed into square');
    // }
//9
   // let answer1=prompt('What is button to right of button "N": ');
    // let answer2=prompt('What is button to the left of button "K": ');
    // let answer3=prompt('What is button to the down of button "/": ');
    //
    // let res=0;
    // if(answer1.toUpperCase()=='M'){
    //     res+=2;
    // }
    // if(answer2.toUpperCase()=='J'){
    //     res+=2;
    // }
    // if(answer3=='8'){
    //     res+=2;
    // }
    //
    // console.log(`Your result: ${res}`);
//10
var now = new Date();
document.write(now.getTime());
/*На экран выводится количество миллисекунд, которые прошли с 1 января 1970 года.
Во многих языках программирования даты хранятся именно в таком формате.
С помощь этого можно работать с датами несегодняшнего дня
Сколько прошло секунд с того момента?*/
var from1970 = now.getTime() / 1000;
/*в одной секунде 1000 миллисекунд, значит нужно разделить на 1000.*/
document.write(from1970);
/*Минуты*/
var from1970 = (now.getTime() / (1000 * 60));
document.write(from1970);
/*Количество часов*/
var from1970 = (now.getTime() / (1000 * 60 * 60));
document.write(from1970);
/*Количество дней*/
var from1970 = (now.getTime() / (1000 * 60 * 60 * 24));
document.write(from1970);
document.write(Math.round(from1970));
/*Это позволяет создавать дату не только для сегодняшнего дня.*/
new Date() /*- объект без параметров, пустые скобки. Значит вся информация в нем по сегодняшнему дню.*/
/*Как узнать, сколько осталось дней до Нового года (включительно до секунд)?*/
var ny = new Date(2022,0,1,0,0,0);
var from1970toNy = (ny.getTime() / (1000 * 60 * 60 * 24));
/*Теперь осталось посчитать разницу.*/
document.write("До Нового года осталось: " + (Math.round(from1970toNy) - Math.round(from1970)) + " дней!");
var week = new Array("Воскресенье","Понедельник","Вторник","Среда","Четверг","Пятница","Суббота");
document.write("" + "Это будет " + week[ny.getDay()] + "");
/*Это вернет день недели, который выпадет на эту дату*/