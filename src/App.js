import React, {Component} from "react";
import axios from "axios";
import ReactDOM from 'react-dom';
import csrfToken from 'django-react-csrftoken';


class App extends Component {
    state = {
        name: '',
    }
   
    handleChange = event => {
        this.setState({ name: event.target.value});
    }
    
    sendGetRequest = () => {
        axios.get("http://localhost:8000/api/todo/")
        .then(res => JSON.parse(res))
        .then(res => this.setState({name: res.data}))
        .catch(err => console.log(err));
    };    
    sendRequest = event => {
        
        event.preventDefault();
        var name = {
            name: this.state.name
        }
        
        axios({
            url: 'http://localhost:8000/api/todos/',
            method: 'post',
            data: { name: "Aditya"},
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            
        })
        .then(res => console.log(res))
        .then(res =>JSON.parse(res))
        .then(res => this.setState({name: res.data}))
        
//        axios.post("http://localhost:8000/api/todos/",name)
//        .catch(err => 
//               console.log(err)
//              );
//        .then(res => console.log(res, "++++"))
//        .then(res => JSON.parse(res))
//        .then(res => this.setState({name: res.data}))
    };

    
    render() {
         return (
             <div> 
              Name 
              <input
             type="text"
             value = {this.state.name}
             onChange= 
             {this.handleChange}
             />
             
             <input 
               type="button"
               value= "Add"
              onClick = 
               {this.sendRequest}
             />
             
             </div>
             
         )
    }
    
}
//
//ReactDOM.render(<App />, document.getElementById('root'));

export default App;