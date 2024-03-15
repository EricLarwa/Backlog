import { React, useState } from 'react'
import { Button } from 'react-bootstrap'
import {BiPlus} from 'react-icons/bi'


const Input = () => {

    const [setName, name] = useState('')
    const [description, setDescription] = useState('')

    const handleNamechange = (event) => {
        setName(event.target.value)
    }

    const handleDecriptionChange = (event) => {
        setDescription(event.target.value)
    }

    const HandleKeyPress = (event) => {
        if (event.key == 'Enter') {
            handleSubmit();
        }
    }
    const handleSubmit = (event) => {
        event.preventDefault();
        console.log("Submitted:", { name })

        setName('')
        setDescription('')
    };

    return (
        <form onSubmit={handleSubmit} className='FormContainer'>
            <div className='inputContainer'>
                <div classnName="btnContainer">
                    <Button variant="primary">
                        <BiPlus />
                    </Button>
                </div>

                <input className='textBox'
                    type="text"
                    value={name}
                    onChange={(event) => setName(event.target.value)}
                    placeholder='Name'
                    onKeyPress={HandleKeyPress}
                />
                <input className="DescBox"
                    type="text"
                    value={description}
                    onChange={(event) => setDescription(event.target.value)}
                    placeholder='Description'
                    onKeyPress={HandleKeyPress}
                />
            </div>
        </form>
    )
}

export default Input;