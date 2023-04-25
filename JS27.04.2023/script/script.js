//! #1
/*
var a=+prompt('input num: ')
var b=+prompt('input num1: ')
function foo(a,b) {
    if (a<b) console.log(-1);
    if (a>b) console.log(1);
    if (a=b) console.log(0);
}
console.log(foo(a,b));
*/
//! #2
/*
var a=+prompt('input num: ')
function factorial(a) {
    var result = 1;
    while(a){
        result *= n--;
    }
    return result;
}
console.log(factorial(a));
*/
//! #3
/*
var a=+prompt('input num1: ')
var b=+prompt('input num2: ')
var c=+prompt('input num3: ')
function str(a,b,c) {
var stroka = `${a}${b}${c}`
}
console.log(str(a,b,c));
*/
//! #4
/*
var a=prompt("input a: ")
var b=prompt("input b: ")

function S(a,b) {
    if(b == 0) {
        return a**2;
    }
    return S=a*b;
    
}
console.log(S(a,b));
console.log(S(a));
*/
//! #5
/*
var a=+prompt('input num: ')

function perfect(num) {
    var temp = 0;
       for(var i=1;i<=num/2;i++) {
        if(num%i === 0) {
            temp += i;
        }
       } 
       if(temp === num && temp !== 0) {
        return "Это идеальное число";
       }
       else {
        return "Это не идеальное число";
       }
}

console.log(perfect(5));
*/
//! #6
/*
var a=+prompt('input begin: ')
var b=+prompt('input end: ')

function perfect(a,b) {
    let result = [];
    for(let i = a; i < b; i++) {
       sum=0;       
       for(let n = 1; n <= i/2; n++) {
        if(i % n === 0) sum += n;
       }
       if(i === sum) result.push(i);
    }
    return result;
}
console.log(perfect(a,b));
*/
//! #7
/*
var h=+prompt('input hours: ')
var m=+prompt('input minutes: ')
var s=+prompt('input seconds: ')
function seconds(h,m,s) {
    if(m == 0) {
        return (`${h}:00:${s}`);
    }
    if(s == 0) {
        return (`${h}:${m}:00`);
    }
    return (`${h}:${m}:${s}`);
}
console.log(seconds(h,m,s));
*/
//! #8
/*
h = +prompt('input часы: ');
m = +prompt('input минуты: ');
s = +prompt('input секунды: ');
function seconds (h,m,s) {
return (h * 3600) + (m * 60) + s;
}
console.log(seconds(h,m,s));
*/
//! #9
/*
s = +prompt('input секунды: ');
function seconds(sec) {
  let s = (sec % 60).toString();
  let m = Math.floor(sec / 60 % 60).toString();
  let h = Math.floor(sec / 60 / 60 % 60).toString();
  return `${h.padStart(2,'0')}:${m.padStart(2,'0')}:${s.padStart(2,'0')}`;

console.log(seconds(sec));
*/
//! #10
var h=+prompt('input hours: ')
var m=+prompt('input minutes: ')
var s=+prompt('input seconds: ')
var h1=+prompt('input hours1: ')
var m1=+prompt('input minutes1: ')
var s1=+prompt('input seconds1: ')
function seconds(h,m,s,h1,m1,s1) {
    if(m == 0) {
        return (`${h}:00:${s}`);
    }
    if(s == 0) {
        return (`${h}:${m}:00`);
    }
    return (`${h}:${m}:${s}`)
    if(m1 == 0) {
        return (`${h1}:00:${s1}`);
    }
    if(s == 0) {
        return (`${h1}:${m1}:00`);
    }
    return (`${h1}:${m1}:${s1}`);
    return dif=(h * 3600) + (m * 60) + s;
    return dif1=(h1 * 3600) + (m1 * 60) + s1;
    return dif2=((h * 3600) + (m * 60) + s)-((h1 * 3600) + (m1 * 60) + s1);
    let s = (dif2 % 60).toString();
  let m = Math.floor(dif2 / 60 % 60).toString();
  let h = Math.floor(dif2 / 60 / 60 % 60).toString();
  return `"Разница: "${h.padStart(2,'0')}:${m.padStart(2,'0')}:${s.padStart(2,'0')}`;
}
console.log(seconds(h,m,s,h1,m1,s1));