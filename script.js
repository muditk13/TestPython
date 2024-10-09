document.getElementById('filterData').addEventListener('click', async () => {
  const startDate = document.getElementById('startDate').value;
  const endDate = document.getElementById('endDate').value;

  const response = await fetch(`/api/data?start=${startDate}&end=${endDate}`);
  const data = await response.json();
  renderChartWithData(data);
});

function renderChartWithData(data) {
  const ctx = document.getElementById('myChart').getContext('2d');
  if (chart) {
    chart.destroy();
  }
  chart = new Chart(ctx, {
    // ... same as before
  });
}
