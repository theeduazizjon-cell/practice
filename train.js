/* A - Task:
 Savol: Shunday 2 parametrli function tuzing , 
 hamda birinchi parametrdagi letterni ikkinchi parametrdagi so'zdan qatnashgan sonini return qilishi kerak boladi.
 MASALAN: countLetter("e", "engineer()") 3ni return qiladi. 
*/

// Masalaning yechimi:
function countLetter(a, b) {
    let count = 0;
    for (let i = 0; i < b.length; i++) {
        if (a === b[i]) count++
    }

    return count
}

console.log(countLetter("e", "engineer"));
