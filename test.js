console.log("hello")

const red_base_url = "https://aiogram-calendar.o-murphy.net"

function sendData(data) {
    console.log(data)
    let query_id = window.Telegram.WebApp.initDataUnsafe.query_id
    // console.log(`https://aiogram-calendar.o-murphy.net/answerWebAppQuery?web_app_query_id=${query_id}&result={}`)


    let result = {"type": "article", "id": "a", "title": "sample", "input_message_content": {"message_text": "Sample"}}

    let uri = `${red_base_url}/answerWebAppQuery?web_app_query_id=${query_id}&result=${JSON.stringify(result)}`
    fetch(uri)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log(data);
        });
}

console.log(window.Telegram.WebApp)
window.Telegram.WebApp.MainButton.setText("Send data")
window.Telegram.WebApp.MainButton.onClick(() => sendData("sadsa"))
window.Telegram.WebApp.MainButton.show()
window.Telegram.WebApp.requestWriteAccess(() => console.log("acc"))

// https://aiogram-calendar.o-murphy.net/answerCallbackQuery?callback_query_id=AAGBQSwDAQAAAIFBLAOBdduU&text=Sample&show_alert=True
// https://api.telegram.org/bot5000479336:AAHA21TniMG8_7_ImWP3y6l31Qr1bPsn0EQ/test/answerWebAppQuery?web_app_query_id=AAGBQSwDAQAAAIFBLAMMiGRS&result={"type": "article", "id": "a", "title": "sample", "input_message_content": {"message_text": "Sample"}}