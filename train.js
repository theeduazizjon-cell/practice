/* B - Task 
Savol:
Shunday function tuzing, u 1 ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin. 
MASALAN: countDigits("ad2a54y79wet0sfgb9")
7 ni return qiladi 
*/

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