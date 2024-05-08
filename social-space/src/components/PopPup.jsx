import React, { useState } from 'react';

const PopUp = () => {
    const [open, setOpen] = useState(true);

    const togglePopup = () => {
        setOpen(!open);
    };

    return (
        <>
            {open && (
                <>
                    <div className='grayed-background' />
                    <div className='info-card'>
                        <h1><u>The Social Space</u></h1>
                        <h3><i>by <a href='https://www.linkedin.com/in/brayden-nguyen'>Brayden Nguyen</a>, <a href='https://www.linkedin.com/in/quentinrl/'>Quentin Romero Lauro</a>, <a href='https://www.linkedin.com/in/shreyash-ranjan/'>Shreyash Ranjan</a>, and <a href='https://www.linkedin.com/in/jeremy-luu1/'>Jeremy Luu</a></i></h3>
                        <p>
                            Hi everyone :)
                            <br />
                            <br />
                            The Social Space is an interactive 3D visualization of the TikTok algorithm through 300,000+
                            scraped videos. The graph is clustered by the frequency that hashtags appear in the same video. They are
                            colored into subcommunities (aka "Toks") using the Louvain algorithm.
                            <br />
                            <br />
                            In the future, we want to be able to take any user's for you page and try to display the Toks they are in
                            and compare with friends. You can check out what that would like like if you click the "User" button in
                            the side bar.
                        </p>
                        <button onClick={togglePopup}>continue</button>
                    </div>
                </>
            )}
        </>
    )
}

export default PopUp;