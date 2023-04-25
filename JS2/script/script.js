//gjj
/*
! gjgjsdksk
? lfjlhllj
iitooio
*/

/*
asu = 3;
let b = 'qwerty';
var c = 123;
const s = 23;

function main(){
   asu = 3;
   let b = 'qwerty';
   var c = 123;
   const s = 23;
   b=79
       const b = 'qwerty';
       asu-=1;

console.log(s);
}

main();

function foo(){
   console.log(asu);
}

*/

/*
String
Number
BigInt
Boolean

Object
Array

null
undefined

infinity

Symbol
*/

/*
let a = 23.78;
a = "qwerty";
console.log(a);
if(typeof(a)=='number'){
   console.log("число")
}
else if(typeof(a)=='string'){
   console.log("текст")
}
*/
/*
let a = BigInt(1242543562131431);
console.log(a);

let b = 1242543562131431;
console.log(b);

let c = 1242543562131431n;
console.log(c);
*/

/*
// < > <= >= == != === !==
*/
/*
let a = 123;
let b = 2;
let c = "3";
console.log(a+b);
*/
/*
let a = prompt("qwerty");
console.log(a+2);
let b = Number(prompt("qwerty"));
console.log(b+2);
let c = +prompt("qwerty");
console.log(c+2);
*/
/*
if(2<6){
   console.log(2);
   console.log(3);
}
console.log("213");

if(2<6)console.log(2);
console.log(3);
console.log("213");
*/
/*
if(a>2){
   console.log(2);
}
else if(a>3){
   console.log(3);
}
else{

}
*/
/*
let a=1;
switch(a){
   case 1:
      console.log(1);
      break;
   case 2:
      console.log(2);
      break;
   default:
      console.log("def");   
}
*/
/*
if (1>3){
   console.log("yes");
}
else{
   console.log("no");
}

(1>3)?console.log("yes"):console.log("no");
console.log((1<3)?"yes":"no");

let res = (1>3)?"yes":"no";
*/
/*
let a = 2**2;
console.log(a);

let b = 2%2;
console.log(b);

let c = Math.floor(3/2);
console.log(c);

let d = 2+2;
console.log(d);
*/
/*
const name="Ivan";
console.log("name",name);
console.log("name",name2);

let a=89;
console.log(`a*2 = ${a*2}`); /* ` шаблоны строк*/

/*
foo(2,3);

function foo(a,b) {
   console.log(123);
   return 123;
}


let a = function foo(a,b) {
   console.log(123);
   return 123;
}

a(2,3);
*/
//summa(2,3);

//console.log(summa(2,3));
/*
function summa(a,b) {
   return (a+b);
}
function dif(a,b) {
   return (a-b);
}
function decor(fun,a,b) {
   console.log(`result: ${fun(a,b)}`);
} 

decor(summa,2,3);
decor(dif,2,3);

console.log(a);
*/
/*
let a=2; 
let b=4;
(function foo(a2,b2) {
   console.log(a2+b2);
})(a,b);
*/
//Стрелочная функция
/*
function  foo(a) {
   return a**2;
}

let c = (a)=>a**2;

console.log(foo(2));
console.log(c(2));
*/
/*
while(2>3){
   continue
   break
}
*/
/*
let a=3;

do{
   console.log(a);
   a+=1;
}while(a>4);
*/
/*
for(let a=2, b; a<4; a+=1) {
   console.log(a);
}
console.log(a);
*/
/*
for(let a=2, b; false;) {
   console.log(a);
}
console.log(a);
*/
/*
let a=2;
let b=4;
console.log(a==2 && b==4);
console.log(a&b);
console.log(a<<b);
*/

// !#1
/*
a=+prompt('input 1-st: ');
b=+prompt('input 2-st: ');
let op=prompt('input operation: ');

switch(op) {
   case '+':
      console.log(`${a}+${b}=${a+b}`);
      break;
   case '-':
      console.log(`${a}-${b}=${a-b}`);
      break;
   case '*':
      console.log(`${a}*${b}=${a*b}`);
      break;
   case '/': 
      if(b==0){
         console.log("div by 0");
      }else{
         console.log(`${a}/${b}=${a/b}`);
      break; 
      }        
   default:
      console.log('unexpected operation');     
}
*/
/*
function max(a,b,c,d) {
   let m = a;
   if(m<b) m=b;
   if(m<c) m=c;
   if(m<d) m=d;
   return m;
}

console.log(max(2,3,4,6));
*/
/*
function max(...ar) {
   let summa = ar[0];
   for (let i=0;i< ar.length; i+=1){
      summa+=ar[i];
   }
   return summa/ar.length;
}
max(2,3,4,6,67,94,24);
*/
//Икремент
/*
let a=3;

let b = ++a;
console.log(a,b);
//Декремент
let a=3;

let b = --a;
console.log(a,b);
*/
//
let a=1;

let b =a++ + ++a;  // a=3 b=4

let c = ++b + ++b + b++; // c=17 b=7
console.log(a,b,c);
console.log(a++, ++b, --c); // a=3 b=8 c=16 