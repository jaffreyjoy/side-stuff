
// ------Trying to promisify the asyncFunc function


// A function performing an async operation
function setTimeoutAsync(params, error, resolve, reject) {
    setTimeout(function() {
        if (err) {
            // console.log("In callback, err = " + err);
            reject(err);
        }
        // console.log("In callback, res = " + res);
        resolve(res);
    }, 3000, res=params, err=error, resolve, reject);
}


// Function to promisify async functions
function promisify(asyncFunction, params, error) {
    let promise = new Promise(function (resolve, reject) { 
        asyncFunction(params, error, resolve, reject);
    });
    return promise;
}
    

// Using the promisify API
let event = promisify(setTimeoutAsync, "params", null);
//let event = promisify(asyncFunc, null, new Error("ma error"));


console.log("No need to wait for asyncFunc to complete");


event.then((res) => {
    console.log("After asyncFunc completes log this for res");
    console.log("res = " + res);
    console.log("Happy Ending");
}).catch((err) => {
    console.log("After asyncFunc completes log this for err");
    console.log("err = " + err);
});





/*

// -------------------------------------Archive------------------------------------- 


// Callback function for asyncFunc function that performs an async operation
function callbackFunc(res, err, resolve, reject) {
    if (err) {
        // console.log("In callback, err = " + err);
        reject(err);
    }
    // console.log("In callback, res = " + res);
    resolve(res);
}


// A function performing an async operation
function setTime(params, error, callbackFunc, resolve, reject) {
    setTimeout(callbackFunc, 3000, params, error, resolve, reject);
}



// Function to promisify async functions
function promisify(asyncFunction, callbackFunc, params, error) {
    let promise = new Promise(function (resolve, reject) {
        asyncFunction(params, error, callbackFunc, resolve, reject);
    });
    return promise;
}


// Using the promisify API
let event = promisify(asyncFunc, callbackFunc, "params", null);
//let event = promisify(asyncFunc, callbackFunc, null, new Error("ma error"));


*/
