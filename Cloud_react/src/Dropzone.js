import React from "react";
import { useDropzone } from "react-dropzone";
import './Dropzone.css';

function Dropzone({ open }) {
  const { getRootProps, getInputProps } = useDropzone({});
  return (
    <div id ="drop_"{...getRootProps({ className: "dropzone" })}>
      <input className="input-zone" {...getInputProps()} />
      <div className="text-center">
        <p className="dropzone-content">
          Drag and drop some files here, or click to select files
        </p>
      </div>
    </div>
  );
  
}

export default Dropzone;