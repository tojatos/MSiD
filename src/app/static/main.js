const create_chart = (handle, data, market) => {
  const div = document.createElement('div');
  div.setAttribute('class', market);
  div.setAttribute('title', market);
  handle.appendChild(div);
  const margin = { top: 50, right: 50, bottom: 50, left: 50 };
  const width = 500;
  const height = 500;
  // add SVG to the page
  const svg = d3
    .select(`.${market}`)
    .append('svg')
    .attr('width', width + margin['left'] + margin['right'])
    .attr('height', height + margin['top'] + margin['bottom'])
  //.call(responsivefy)
    .append('g')
    .attr('transform', `translate(${margin['left']},  ${margin['top']})`);
  // find data range
  const xMin = d3.min(data, d => {
    return d['date'];
  });
  const xMax = d3.max(data, d => {
    return d['date'];
  });
  const yMin = d3.min(data, d => {
    return d['buy'];
  });
  const yMax = d3.max(data, d => {
    return d['sell'];
  });
  // scales for the charts
  const xScale = d3
    .scaleTime()
    .domain([xMin, xMax])
    .range([0, width]);
  const yScale = d3
    .scaleLinear()
    .domain([yMin - 5, yMax])
    .range([height, 0]);
  // create the axes component
  svg
    .append('g')
    .attr('id', 'xAxis')
    .attr('transform', `translate(0, ${height})`)
    .call(d3.axisBottom(xScale));
  svg
    .append('g')
    .attr('id', 'yAxis')
    .attr('transform', `translate(${width}, 0)`)
    .call(d3.axisRight(yScale));

  // generates close price line chart when called
  const buyLine = d3
    .line()
    .x(d => {
      return xScale(d['date']);
    })
    .y(d => {
      return yScale(d['buy']);
    });

  const sellLine = d3
    .line()
    .x(d => {
      return xScale(d['date']);
    })
    .y(d => {
      return yScale(d['sell']);
    });
  // Append the path and bind data
  svg
    .append('path')
    .data([data])
    .style('fill', 'none')
    .attr('id', 'buyChart')
    .attr('stroke', 'steelblue')
    .attr('stroke-width', '1.5')
    .attr('d', buyLine);

  svg
    .append('path')
    .data([data])
    .style('fill', 'none')
    .attr('id', 'sellChart')
    .attr('stroke', 'red')
    .attr('stroke-width', '1.5')
    .attr('d', sellLine);

}
