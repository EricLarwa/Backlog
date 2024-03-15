import React from "react";
import { Button } from "react-bootstrap";
import { FaTrash } from "react-icons/fa";

const HeaderArea= ({name, showDeleteButton ,onDelete }) => {
    const handleDelete = () => {
        onDelete();
    }    
    return (
       <div className="headerArea">
         <h2>{name}</h2>
         {showDeleteButton && (
         <Button variant="danger" onClick={handleDelete}>
            <FaTrash /> Delete
         </Button>
         )}
       </div>
    );
};

export default HeaderArea;