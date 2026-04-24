/* 

D - Task 
Savol: 
Shunday function tuzingki unga integraldan iborat array pass bolsin 
va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin 
Masalan: gethighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini 

*/

// Masalaning yechimi 

function getHighestIndex(arr) {
    let max = arr[0];
    let index = 0;

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
            index = i;
        }
    }
    return index;
}

console.log(getHighestIndex([5, 21, 12, 21, 8]));


/* 
C - Task
Savol:
Shunday function tuzing, u 2 ta string parametr ga ega bolsin, hamda 
agar har ikkala string bir hil harfladan iborat bolsa true, aks holda 
false qaytarsin 
Masalan: checkContent("mitgroup","gmtiptou") 
true ni return qiladi 
*/

/* 
Masalaning yechimi 

function checkContent(str1, str2) {
    if (str1.length !== str2.length) {
        return false;
    }

    let sortedstr1 = str1.split('').sort().join('');
    let sortedstr2 = str2.split('').sort().join('');

    return sortedstr1 === sortedstr2;
}

console.log(checkContent("mitgroup", ("gmtiprou")))


/* B - Task 
Savol:
Shunday function tuzing, u 1 ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin. 
MASALAN: countDigits("ad2a54y79wet0sfgb9")
7 ni return qiladi 

function countDigits(str) {
    let count = 0;

    for (let char of str) {
        if (char >= '0' && char <= '9') {
            count++;
        }
    }
    return count;
}
console.log(countDigits("ad2a54y79wet0sfgb9"));
*/

/* A - Task:
 Savol: Shunday 2 parametrli function tuzing , 
 hamda birinchi parametrdagi letterni ikkinchi parametrdagi so'zdan qatnashgan sonini return qilishi kerak boladi.
 MASALAN: countLetter("e", "engineer()") 3ni return qiladi. 
*/

/* 

Masalaning yechimi:
function countLetter(a, b) {
    let count = 0;
    for (let i = 0; i < b.length; i++) {
        if (a === b[i]) count++
    }

    return count
}

console.log(countLetter("e", "engineer"));

*/