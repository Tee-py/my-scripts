const ALPHABETS = "abcdefghijklmnopqrstuvwxyz";

function createEncodeMapping(shift){
    result = {}
    for(i=0; i<ALPHABETS.length; i++){
        index = (i+shift)%ALPHABETS.length
        result[ALPHABETS[i]] = ALPHABETS[index]
    }
    return result;
}

function createDecodeMapping(shift){
    result = {}
    for(i=0; i<ALPHABETS.length; i++){
        index = i-shift
        if (index<0){
            index += 26
        }
        result[ALPHABETS[i]] = ALPHABETS[index]
    }
    return result;
}

function encode(str, n){
    let result = "";
    str = str.toLowerCase();
    encodeMap = createEncodeMapping(n);
    for (char of str){
        if (char == " "){
            result += char
        } else{
            result += encodeMap[char]
        }
    }
    return result;
}

function decode(str, n){
    let result = "";
    str = str.toLowerCase();
    decodeMap = createDecodeMapping(n);
    for (char of str){
        if (char == " "){
            result += " "
        } else {
            result += decodeMap[char]
        }  
    }
    return result;
}

const test = () => {
    test_arr = [
        "mother", 
        "father", 
        "children", 
        "blockchain", 
        "bridge", 
        "consensus", 
        "staking", 
        "liquidy", 
        "supply",
        "Proof Of Work",
        "Proof Of Stake"
    ]
    for (word of test_arr){
        encoded = encode(word, 3)
        decoded = decode(encoded, 3)
        if (decoded !== word.toLowerCase()){
            console.log(`Test Failed For Word ${word}`)
            return false
        }
    }
    console.log("All Test Passed")
    return true
}

test()