import { React, useState } from 'react'
import { Button } from 'react-bootstrap'
import { BiPlus } from 'react-icons/bi'


const Input = () => {

    const [columns, setColumns] = useState([
        [{ type: 'header', content: 'Column 1' }],
        [{ type: 'card', content: 'Card 1' }]
      ]);

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
    
      return (
        <div className="container">
        {columns.map((column, columnIndex) => (
            <div key={columnIndex} className="column">
            {column.map((item, cardIndex) => (
                <div key={cardIndex}>
                {item.type === 'header' ? (
                    <input
                    type="text"
                    className="header"
                    placeholder={item.content}
                    />
                ) : (
                    <input
                    type="text"
                    className="card"
                    placeholder={`Card ${cardIndex + 1}`}
                    value={item.content}
                    onChange={(event) => handleChange(event, columnIndex, cardIndex)}
                    />

                )}
                </div>
            ))}
            <button onClick={() => addCard(columnIndex)}>Add Card</button>
            </div>
        ))}
        </div>
      );
}

export default Input;