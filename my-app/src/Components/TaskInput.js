import { React, useState } from 'react'
import { Button} from 'react-bootstrap'
import { FaTrash } from 'react-icons/fa'
import HeaderArea from './HeaderArea'

const Input = () => {

    const [columns, setColumns] = useState([
        [{ type: 'header', content: 'To-do' }],
        [{ type: 'header', content: 'Progress' }],
        [{ type: 'header', content: 'Done' }]
    ])

    const addCard = (columnIndex) => {
        const newColumns = [...columns];
        newColumns[columnIndex].push({ type: 'card', content: '' });
        setColumns(newColumns);
    };

    const handleChange = (event, columnIndex, cardIndex) => {
        const newColumns = [...columns];
        newColumns[columnIndex][cardIndex].content = event.target.value;
        setColumns(newColumns);
    };

    const handleDeleteCard = (columnIndex) => (cardIndex) =>{
        console.log('Deleteing card:', columnIndex, cardIndex);
        const newColumns =[...columns];
        newColumns[columnIndex].splice(cardIndex, 1);
        console.log("New Columns:", newColumns);
        setColumns(newColumns);
    }
    
      return (
        <div className="container">
            {columns.map((column, columnIndex) => (
                <div key={columnIndex} className="column">
                    {column.map((item, cardIndex) => (
                        <div key={cardIndex}>
                            {item.type === 'header' ? (
                                <HeaderArea name={item.content} showDeleteButton={false}/>
                            ) : (
                                <div>
                                    <input
                                        type="text"
                                        className="card"
                                        placeholder={`Card ${cardIndex + 1}`}
                                        value={item.content}
                                        onChange={(event) => handleChange(event, columnIndex, cardIndex)}
                                    />
                                    <Button variant="danger" onClick={() => handleDeleteCard(columnIndex)(cardIndex)} className='btn1'>
                                        <FaTrash />
                                    </Button>
                                </div>
                            )}
                        </div>
                    ))}
                    <button onClick={() => addCard(columnIndex)}>Add Card</button>
                </div>
            ))}
        </div>
      );
};

export default Input;