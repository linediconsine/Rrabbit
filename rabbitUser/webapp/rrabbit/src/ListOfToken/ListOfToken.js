import React from 'react'

class ListOfToken extends React.Component {

    constructor(props) {
      super(props);
      this.state = {
        keys: [],
        message : "Waiting for fetch the data from RR User "
      };
    }
  
    componentDidMount() {
      
          const self = this;
          setInterval(() => { 
            fetch("http://127.0.0.1:5000/json", {  method: 'get' } )
            .then(res => res.json())
            .then(
                (result) => {
                    console.log(result);
                    self.setState({
                        message : `User have recived ${result.keys.length} keys`,
                        keys: result.keys
                    });
                    },
                (error) => {
                    self.setState({
                        message : 'Something is not right...',
                        keys : []});
                    } 
                );



           },1000);
    }

    render() {
      const { message, keys } = this.state;
      const JSXmessage =  message ? <h2 className="message">{message}</h2> : ""
      
      return (
      <article>
            {JSXmessage}
            <ul className="keys">
                    {keys.map( (item,index) => (
                        <li key={item + index}>
                            {item} - {index}
                        </li>
                    ))}
            </ul>
      </article>)
    }
  }

  export default ListOfToken;