/*
Asynchronous function: Callback, Async and promise 

    Define           Call 
    callback         function 
    async/await      then/catch 
    promise          then/watch 

*/

// define 

function division(a, b, callback) {
    if (b === 0) {
        callback("Not Devided by zero", null)
    } else {
        callback(null, a % b)
    }
}

console.log("passed here A");
// call 
division(10, 3, function (err, data) {
    if (err) console.log("ERROR:", err);
    else {
        setTimeout(function () {
            console.log("passed here B ");
            console.log("RESULT:", data);
            console.log("...");
        }, 2000);


    }
});
console.log("passed here C");


async function division(a, b) {
    return new Promise(Resolve, reject) => {

        if (b === 0) {
            throw new Error("Not divided by zero");

        } else {
            setInterval(function () {
                resolve(a % b);
            }, 2000)
        }
    }
}

division(10, 3).then(data => {
    console.log("Result:", data);
    console.log("....")

    division(10, 4.then(data => {
        console.log("Result:", data);
        console.log("....")
    }).catch(err => {
        console.log("Error division:", err);
    });
    division(20, 7).then(data => {
        console.log("Result:", data);
        console.log("....")
    }).catch(err => {
        console.log("Error division:", err);
    });
}).catch(err => {
    console.log("Error division:", err);
});


function division(a, b) {
    if (b === 0) {
        throw new Error("Not Devided by zero")
    } else {
        return a % b
    }
}

async function run() {
    let result = await division(10, 3);
    console.log("result one:", result);

    result = await division(10, 4);
    console.log("result one:", result);

    result = await division(20, 7);
    console.log("result one:", result);

}
run();