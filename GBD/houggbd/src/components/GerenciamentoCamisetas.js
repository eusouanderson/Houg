import React, { useState, useEffect } from 'react';
import './GerenciamentoCamisetas.css';

const GerenciamentoCamisetas = () => {
  const [camisetas, setCamisetas] = useState([]);
  const [nome, setNome] = useState('');
  const [modelo, setModelo] = useState('');
  const [preco, setPreco] = useState('');
  const [tamanho, setTamanho] = useState('');
  const [imagem, setImagem] = useState(null);

  useEffect(() => {
    const mockCamisetas = [
      { id: 1, nome: 'Camiseta Azul', modelo: 'Básica', preco: 25.99, tamanho: 'M', imagem: 'https://via.placeholder.com/150' },
      { id: 2, nome: 'Camiseta Vermelha', modelo: 'Listrada', preco: 29.99, tamanho: 'L', imagem: 'https://via.placeholder.com/150' },
      { id: 3, nome: 'Camiseta Verde', modelo: 'Estampada', preco: 22.99, tamanho: 'S', imagem: 'https://via.placeholder.com/150' }
    ];
    setCamisetas(mockCamisetas);
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    const reader = new FileReader(); 
    reader.onload = function () {
      const novaCamiseta = {
        id: camisetas.length + 1,
        nome: nome,
        modelo: modelo,
        preco: parseFloat(preco),
        tamanho: tamanho,
        imagem: reader.result 
      };
      setCamisetas([...camisetas, novaCamiseta]);
    };
    reader.readAsDataURL(imagem); 
    setNome('');
    setModelo('');
    setPreco('');
    setTamanho('');
    setImagem(null);
  };

  const handleLimparCamisetas = () => {
    setCamisetas([]);
  };

  return (
    <div className="container">
      <nav className="nav">
        <h1>Houg</h1>
      </nav>
      <h2>Gerenciamento do Banco de Dados</h2>
      <form className="form" onSubmit={handleSubmit}>
        <label>
          Nome:
          <input className="input-text" type="text" value={nome} onChange={(e) => setNome(e.target.value)} />
        </label>
        <br />
        <label>
          Modelo:
          <input className="input-text" type="text" value={modelo} onChange={(e) => setModelo(e.target.value)} />
        </label>
        <br />
        <label>
          Preço:
          <input className="input-number" type="number" value={preco} onChange={(e) => setPreco(e.target.value)} />
        </label>
        <br />
        <label>
          Tamanho:
          <input className="input-text" type="text" value={tamanho} onChange={(e) => setTamanho(e.target.value)} />
        </label>
        <br />
        <label>
          Imagem:
          <input className="input-file" type="file" accept="image/*" onChange={(e) => setImagem(e.target.files[0])} />
        </label>
        <br />
        <button className="button-submit" type="submit">Adicionar Camiseta</button>
      </form>
      
      <button className="button-limpar" onClick={handleLimparCamisetas}>Limpar Camisetas</button>
      
      <h3>Camisetas Disponíveis:</h3>
      <table className="camisetas-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Modelo</th>
            <th>Preço</th>
            <th>Tamanho</th>
            <th>Imagem</th>
          </tr>
        </thead>
        <tbody>
          {camisetas.map(camiseta => (
            <tr key={camiseta.id}>
              <td>{camiseta.id}</td>
              <td>{camiseta.nome}</td>
              <td>{camiseta.modelo}</td>
              <td>R${camiseta.preco.toFixed(2)}</td>
              <td>{camiseta.tamanho}</td>
              <td><img src={camiseta.imagem} alt="Imagem Camiseta" style={{ width: '150px', height: '150px' }} /></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default GerenciamentoCamisetas;
