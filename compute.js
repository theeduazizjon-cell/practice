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

// call 
division(10, 3, function (err, data) {
    if (err) console.log("ERROR:", err);
    else {
        console.log("RESULT:", data);
        console.log("...");


        division(10, 4, function (err, data) {
            if (err) console.log("ERROR:", err);
            else {
                console.log("RESULT:", data);
                console.log("...");


                division(20, 7, function (err, data) {
                    if (err) console.log("ERROR:", err);
                    else {
                        console.log("RESULT:", data);
                        console.log("...");
                    }

                });
            }

        });
    }

});