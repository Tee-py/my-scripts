const { ethers } = require("ethers");

const main = async() => {
    const provider = new ethers.providers.JsonRpcProvider('http://127.0.0.1:7545');
    const signer = provider.getSigner()
    let balance = await signer.getBalance()
    const addr = await signer.getAddress()
    const txCount = await signer.getTransactionCount()
    balance = ethers.utils.formatEther(balance.toString())
    console.log("\x1b[32m", `Account Balance -> ${balance} Ether`)
    console.log("\x1b[31m", `Account Address -> ${addr}`)
    console.log("\x1b[34m", `Nonce -> ${txCount}`)
    

    // Play With Nonce
    const tx = await signer.sendTransaction({
        to: "0x537c949aa3bAa76EfB643075385030A5f5DAC750",
        value: ethers.utils.parseEther("90"),
        nonce: txCount + 1
    });
    console.log("\x1b[31m", `Nonce After Tx is -> ${await signer.getTransactionCount()}`)

    
}

main()
