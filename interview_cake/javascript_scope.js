// question link: https://www.interviewcake.com/question/python3/js-scope?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email&__s=nywctklrkfaexchucj9e&utm_source=drip&utm_medium=email&utm_campaign=Interview+Cake+Weekly+Problem+%23618%3A+JavaScript+Scope
var text = 'outside';
function logIt(){
    console.log(text);
    //var text = 'inside';
};
logIt();

if (require.main === module) {
    logIt();
}