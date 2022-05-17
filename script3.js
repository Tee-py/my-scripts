
function func1() {
    console.log('Completed Func 1')
}

async function func2() {
    res = 0
    for (i=0; i<3; i++) {
        res += i
    }
    return res
}



runFunc2 = async() => {
    res = await func2();
    console.log(res)
}

runFunc2()
func1()
