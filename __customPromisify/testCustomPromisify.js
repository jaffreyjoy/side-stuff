
// Callback function for asyncFunc function that performs an async operation
function callbackFunc(res, err) {
    if(err) {
        console.log("in callback err = " + err);
        throw err;
    }
    console.log("Result is " + res);
    return res;
}


// A function performing an async operation
function asyncFunc(params, callbackFunc) {
    setTimeout(callbackFunc, 3000, null, new Error());
}

//call asyncFunc
console.log(asyncFunc("params", callbackFunc));

console.log("No need to wait for asyncFunc to complete");

console.log("After asyncFunc completes log this");

console.log("Happy Ending");





// ------Trying to promisify the asyncFunc function



// Callback function for asyncFunc function that performs an async operation
function callbackFunc(res, err, resolve, reject) {
    if (err) {
        console.log("in callback err = " + err);
        reject(err);
    }
    console.log("Result is " + res);
    resolve(res);
}


// A function performing an async operation
function asyncFunc(params, callbackFunc, resolve) {
    setTimeout(callbackFunc, 3000, null, new Error(), resolve, reject);
}


// Function to promisify async functions
function promisify(asyncFunction) {
    let promise = new Promise(function (resolve, reject) { 
        asyncFunction("params", callbackFunc, resolve, reject);
    });
    return promise;
}
    



