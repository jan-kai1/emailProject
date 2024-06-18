import { useEffect, useState } from "react"
function DisplayEmail ({emails, page = 1}) {
    let realPage = page -1
    // tkae 0-5  5-10..
    let displayedEmails = emails.slice(realPage * 5, realPage * 5 + 5)
    if (!emails) {
        return (<div>NO EMAILS FOUND</div>)
    } else {
        
        return(
            <ul>

                {displayedEmails.map(email => {
                    return (
                        <li key = {email.snippet}>
                            <p>{email.sender}</p>
                            {/* <p>{email.plain ? email.plain : "no preview"}</p> */}
                            <p>{email.summary ? email.summary : "no preview"}</p>
                        </li>
                    )
                })}
            </ul>
                
            
        )
    }

}

export default DisplayEmail